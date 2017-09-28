from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import *
from dimecapp.forms import DesocupadoForm
from django.db import transaction

@login_required
def home(request):
    return render(request, 'home.html')

@transaction.atomic
def create_user_view(request):
    if request.method == 'POST':
        #user_form = UserCreationForm(request.POST)
        form = DesocupadoForm(request.POST)
        if form.is_valid():
            user = Desocupado(
                nombre = form.cleaned_data.get('nombre'),
                apellido = form.cleaned_data.get('apellido'),
                fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento'),
                dni = form.cleaned_data.get('dni'),
                email = form.cleaned_data.get('email')
            )
            user.save()
            user.refresh_from_db()  # This will load the Desocupado created by the Signal
            #desocupado_form = DesocupadoForm(request.POST, instance=user.desocupado)  # Reload the desocupado form with the desocupado instance
            #desocupado_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            #desocupado_form.save()  # Gracefully save the form
    else:
        #user_form = UserCreationForm()
        form = DesocupadoForm()
    return render(request, 'signup.html', {
       # 'user_form': user_form,
        'form': form
})
