from django.contrib import admin
from .models import Validacion


@admin.register(Validacion)
class ValidacionAdmin(admin.ModelAdmin):
    list_display = (
        "evidencia",
        "revisor",
        "aprobada",
        "revisada_en",
    )
    list_filter = (
        "aprobada",
        "revisada_en",
    )
    search_fields = (
        "evidencia__actividad__titulo",
        "observacion",
    )