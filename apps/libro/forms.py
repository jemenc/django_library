
from django import forms
from .models import Autor

#Autogenerar el codigo html
class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = ['nombre','apellido','nacionalidad','descripcion']