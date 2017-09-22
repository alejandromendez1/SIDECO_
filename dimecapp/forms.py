from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    apellido = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    dni = forms.IntegerField(required=True)
    nacimiento = forms.DateField(required=True)
    profesion = forms.CharField(max_length=200, required=False)
    experiencia_laboral = forms.CharField(widget=forms.Textarea, max_length=700, required=False)
    formacion = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    habilidades = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    email = forms.EmailField(max_length=254, help_text='Requerido, por favor ingrese un email valido.')

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'email', 'password1', 'password2', )