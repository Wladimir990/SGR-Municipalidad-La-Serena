from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.iniciar_sesion,
        name="login"
    ),

    path(
        "cerrar-sesion/",
        views.cerrar_sesion_sgr,
        name="cerrar_sesion"
    ),

    path(
        "funcionario/",
        views.panel_funcionario,
        name="panel_funcionario"
    ),

    path(
        "funcionario/actividad/nueva/",
        views.crear_actividad,
        name="crear_actividad"
    ),

    path(
        "funcionario/actividades/",
        views.mis_actividades,
        name="mis_actividades"
    ),

    path(
        "funcionario/evidencia/nueva/",
        views.subir_evidencia,
        name="subir_evidencia"
    ),

    path(
        "verificador/",
        views.panel_verificador,
        name="panel_verificador"
    ),

    path(
        "verificador/validaciones/",
        views.ver_validaciones,
        name="ver_validaciones"
    ),

    path(
        "verificador/validacion/nueva/",
        views.crear_validacion,
        name="crear_validacion"
    ),
]