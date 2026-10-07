from django.db import models
from django.conf import settings 
import uuid 


class Actividad(models.Model):
    codigo = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    funcionario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="actividades"
    )

    titulo = models.CharField(max_length=150)

    descripcion = models.TextField()

    fecha_actividad = models.DateField()

    lugar = models.CharField( max_length=200 )

    contacto = models.CharField(
        max_length=150,
        blank=True
    )

    observaciones = models.TextField(
        blank=True
    )

    creado_en = models.DateTimeField(
        auto_now_add=True
    )

    class Estado(models.TextChoices):
        BORRADOR = "BORRADOR", "borrador"
        PENDIENTE = "PENDIENTE", "Pendiente"
        APROBADA = "APROBADA", "Aprobada"
        RECHAZADA = "RECHAZADA", "Rechazada"

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.BORRADOR
    )
    def __str__(self):
        return f"{self.codigo} -  {self.titulo}"


class Evidencia(models.Model):
    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        related_name="evidencias"
    )

    archivo = models.ImageField(
        upload_to="evidencias/"
    )

    descripcion = models.CharField(
        max_length=250,
        blank=True
    )

    subida_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="evidencias_subidas"
    )

    creada_en = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Evidencia de {self.actividad.titulo}"