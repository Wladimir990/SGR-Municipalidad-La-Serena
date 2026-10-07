from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import ActividadForm, EvidenciaForm, ValidacionForm
from validations.models import Validacion


def iniciar_sesion(request):

    if request.user.is_authenticated:

        if request.user.groups.filter(name="Funcionario").exists():
            return redirect("panel_funcionario")

        if request.user.groups.filter(name="Verificador").exists():
            return redirect("panel_verificador")

    mensaje_error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:

            login(request, usuario)

            if usuario.groups.filter(name="Funcionario").exists():
                return redirect("panel_funcionario")

            if usuario.groups.filter(name="Verificador").exists():
                return redirect("panel_verificador")

            logout(request)

            mensaje_error = (
                "Tu cuenta no tiene un perfil habilitado "
                "para ingresar al sistema."
            )

        else:

            mensaje_error = "Usuario o contraseña incorrectos."

    return render(
        request,
        "activities/login.html",
        {
            "mensaje_error": mensaje_error
        }
    )


@login_required
def cerrar_sesion_sgr(request):

    logout(request)

    return redirect("login")


@login_required
def panel_funcionario(request):

    es_funcionario = request.user.groups.filter(
        name="Funcionario"
    ).exists()

    if not es_funcionario:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    return render(
        request,
        "activities/panel_funcionario.html"
    )


@login_required
def panel_verificador(request):

    es_verificador = request.user.groups.filter(
        name="Verificador"
    ).exists()

    if not es_verificador:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    return render(
        request,
        "activities/panel_verificador.html"
    )


@login_required
def crear_actividad(request):

    es_funcionario = request.user.groups.filter(
        name="Funcionario"
    ).exists()

    if not es_funcionario:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    if request.method == "POST":

        formulario = ActividadForm(request.POST)

        if formulario.is_valid():

            actividad = formulario.save(commit=False)

            actividad.funcionario = request.user

            actividad.save()

            return redirect("mis_actividades")

    else:

        formulario = ActividadForm()

    return render(
        request,
        "activities/crear_actividad.html",
        {
            "formulario": formulario
        }
    )


@login_required
def mis_actividades(request):

    es_funcionario = request.user.groups.filter(
        name="Funcionario"
    ).exists()

    if not es_funcionario:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    actividades = request.user.actividades.all().order_by(
        "-fecha_actividad"
    )

    return render(
        request,
        "activities/mis_actividades.html",
        {
            "actividades": actividades
        }
    )


@login_required
def subir_evidencia(request):

    es_funcionario = request.user.groups.filter(
        name="Funcionario"
    ).exists()

    if not es_funcionario:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    if request.method == "POST":

        formulario = EvidenciaForm(
            request.POST,
            request.FILES
        )

        formulario.fields["actividad"].queryset = (
            request.user.actividades.all()
        )

        if formulario.is_valid():

            evidencia = formulario.save(commit=False)

            evidencia.subida_por = request.user

            evidencia.save()

            return redirect("panel_funcionario")

    else:

        formulario = EvidenciaForm()

        formulario.fields["actividad"].queryset = (
            request.user.actividades.all()
        )

    return render(
        request,
        "activities/subir_evidencia.html",
        {
            "formulario": formulario
        }
    )


@login_required
def ver_validaciones(request):

    es_verificador = request.user.groups.filter(
        name="Verificador"
    ).exists()

    if not es_verificador:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    validaciones = Validacion.objects.select_related(
        "evidencia",
        "revisor"
    ).order_by(
        "-revisada_en"
    )

    return render(
        request,
        "activities/ver_validaciones.html",
        {
            "validaciones": validaciones
        }
    )


@login_required
def crear_validacion(request):

    es_verificador = request.user.groups.filter(
        name="Verificador"
    ).exists()

    if not es_verificador:

        return render(
            request,
            "activities/sin_permiso.html"
        )

    if request.method == "POST":

        formulario = ValidacionForm(request.POST)

        if formulario.is_valid():

            validacion = formulario.save(commit=False)

            validacion.revisor = request.user

            validacion.save()

            return redirect("ver_validaciones")

    else:

        formulario = ValidacionForm()

    return render(
        request,
        "activities/crear_validacion.html",
        {
            "formulario": formulario
        }
    )