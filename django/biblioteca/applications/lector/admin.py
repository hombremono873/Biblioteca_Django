from django.contrib import admin

from applications.lector.models import Lector, Prestamo

# Register your models here.
admin.site.register(Lector)
admin.site.register(Prestamo)