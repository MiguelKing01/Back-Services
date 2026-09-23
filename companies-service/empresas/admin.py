from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_company',
        'nit_company',
        'correo_company',
        'firebase_uid',
        'activo',
        'fecha_creacion',
    )

    list_filter = ('activo',)

    search_fields = (
        'nombre_company',
        'nit_company',
        'correo_company',
        'firebase_uid',
    )

    readonly_fields = ('fecha_creacion',)

    fields = (
        'nit_company',
        'nombre_company',
        'correo_company',
        'telefono_company',
        'firebase_uid',
        'activo',
        'fecha_creacion',
    )