from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion", "estado")
    list_filter = ("estado", "fecha_publicacion", "autor")
    search_fields = ("titulo", "contenido")
    ordering = ("-fecha_publicacion",)