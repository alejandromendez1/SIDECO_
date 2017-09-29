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
def signup(request):
    if request.method == 'POST':
        form = DesocupadoForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.desocupado.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
    else:
        form = DesocupadoForm()
    return render(request, 'signup.html', {'form': form})
