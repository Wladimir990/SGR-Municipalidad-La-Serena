from django.db import models
from django.conf import settings
from activities.models import Evidencia


class Validacion(models.Model):
    evidencia = models.OneToOneField(
        Evidencia,
        on_delete=models.CASCADE,
        related_name="validacion"
    )

    revisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="validaciones_realizadas"
    )

    aprobada = models.BooleanField()

    observacion = models.TextField(
        blank=True
    )

    revisada_en = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        estado = "Aprobada" if self.aprobada else "Rechazada"
        return f"{self.evidencia} - {estado}"