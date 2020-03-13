from django.db import models

# Create your models here.
# Clase de python que va conectar una base de datos
# Como ejecutar un archivo que no corresponda a una base de datos

class Autor(models.Model):

    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200,blank =  False,null = False) #var char
    apellido = models.CharField(max_length = 220,blank =  False,null = False)
    nacionalidad = models.CharField(max_length = 100,blank =  False,null = False)
    descripcion = models.TextField(blank = False, null = False)
    estado = models.BooleanField('Estado', default=True)
    fecha_de_creacion = models.DateField('Fecha de creacion',auto_now=True,auto_now_add= False)

    class Meta:   #Datos extras de nuestro modelo

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Libro(models.Model):

    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo',max_length = 255,blank = False, null = False)
    fecha_de_publicacion = models.DateField('Fecha de publicacion',blank = False, null = False)
    genero = models.CharField('Genero',max_length = 100, blank = False, null = False)
    #Relacion uno a uno
    #autor_id = models.OneToOneField(Autor, on_delete= models.CASCADE) #el argumento on_delete me indica que se debe hacer cuando se borra un elemento relacionado
    #Relacion una a muchos
    #autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE) #el argumento on_delete me indica que se debe hacer cuando se borra un elemento relacionado
    #Relacion de muchos a muchos
    autor_id = models.ManyToManyField(Autor) #el argumento on_delete no se requiere aqui
    fecha_de_creacion = models.DateField('Fecha de creacion',auto_now=True,auto_now_add= False)

    class Meta:

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

        def __str__(self):
            return self.titulo


