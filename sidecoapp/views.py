from django.shortcuts import render
from .models import *

def trabajos_lista(request):
    return render(request, 'sidecoapp/trabajos_lista.html', {})
