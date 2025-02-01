from django.contrib import admin

from applications.libro.models import Categoria, Libro

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Libro)