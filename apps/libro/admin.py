from django.contrib import admin
from .models import Autor,Libro


admin.site.register(Autor) #Se estan creando el modelo en la administacion de django
admin.site.register(Libro)

# Register your models here.
