from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DesocupadoForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    apellido = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    dni = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    profesion = forms.CharField(max_length=200, required=False)
    experiencia_laboral = forms.CharField(widget=forms.Textarea, max_length=700, required=False)
    formacion = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    habilidades = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido, por favor ingrese un email valido.')

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'dni', 'fecha_nacimiento', 'profesion', 'experiencia_laboral', 'formacion', 'habilidades', 'email', 'password1', 'password2')
