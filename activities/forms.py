from django import forms

from .models import Actividad, Evidencia
from validations.models import Validacion


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad

        fields = [
            "titulo",
            "descripcion",
            "fecha_actividad",
            "lugar",
            "contacto",
            "observaciones",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "campo-formulario",
                    "placeholder": "Ej: Reunión con junta de vecinos",
                }
            ),

            "descripcion": forms.Textarea(
                attrs={
                    "class": "campo-formulario",
                    "rows": 5,
                    "placeholder": "Describe la actividad",
                }
            ),

            "fecha_actividad": forms.DateInput(
                attrs={
                    "class": "campo-formulario",
                    "type": "date",
                }
            ),

            "lugar": forms.TextInput(
                attrs={
                    "class": "campo-formulario",
                    "placeholder": "Lugar de la actividad",
                }
            ),

            "contacto": forms.TextInput(
                attrs={
                    "class": "campo-formulario",
                    "placeholder": "Persona o teléfono de contacto",
                }
            ),

            "observaciones": forms.Textarea(
                attrs={
                    "class": "campo-formulario",
                    "rows": 4,
                    "placeholder": "Observaciones adicionales",
                }
            ),
        }


class EvidenciaForm(forms.ModelForm):
    class Meta:
        model = Evidencia

        fields = [
            "actividad",
            "archivo",
            "descripcion",
        ]

        widgets = {
            "actividad": forms.Select(
                attrs={
                    "class": "campo-formulario",
                }
            ),

            "archivo": forms.ClearableFileInput(
                attrs={
                    "class": "campo-formulario",
                }
            ),

            "descripcion": forms.Textarea(
                attrs={
                    "class": "campo-formulario",
                    "rows": 4,
                    "placeholder": "Describe brevemente la evidencia",
                }
            ),
        }


class ValidacionForm(forms.ModelForm):
    class Meta:
        model = Validacion

        fields = [
            "evidencia",
            "aprobada",
            "observacion",
        ]

        widgets = {
            "evidencia": forms.Select(
                attrs={
                    "class": "campo-formulario",
                }
            ),

            "aprobada": forms.CheckboxInput(
                attrs={
                    "class": "checkbox-validacion",
                }
            ),

            "observacion": forms.Textarea(
                attrs={
                    "class": "campo-formulario",
                    "rows": 5,
                    "placeholder": "Ingrese una observación sobre la revisión realizada",
                }
            ),
        }