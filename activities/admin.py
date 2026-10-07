from django.contrib import admin
from .models import Actividad, Evidencia


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "funcionario",
        "fecha_actividad",
        "estado",
        "creado_en",
    )
    list_filter = (
        "estado",
        "fecha_actividad",
    )
    search_fields = (
        "titulo",
        "descripcion",
        "lugar",
    )


@admin.register(Evidencia)
class EvidenciaAdmin(admin.ModelAdmin):
    list_display = (
        "actividad",
        "subida_por",
        "creada_en",
    )
    search_fields = (
        "actividad__titulo",
        "descripcion",
    )