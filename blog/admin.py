from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo", "autor", "fecha_publicacion", "estado")
    search_fields = ("titulo", "subtitulo", "contenido")
    list_filter = ("estado", "fecha_publicacion")