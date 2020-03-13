from django.urls import path,re_path
#from .views import Home
from .views import crearAutor,listarAutor,editarAutor,eliminarAutor

urlpatterns = [
    #path('',Home,name = 'index')
    path('crear_autor',crearAutor,name = 'crear_autor' ),
    path('listar_autor',listarAutor,name = 'listarAutor' ),
    path('editar_autor/<int:id>',editarAutor,name = 'editar_autor'),
    path('eliminar_autor/<int:id>',eliminarAutor,name = 'eliminar_autor')
]


#re_path -> permite versiones regulares
#path('listar_autor/<slug:string/int:pk>',listarAutor,name = 'listarAutor' )