from django.shortcuts import render

def trabajos_lista(request):
    return render(request, 'sidecoapp/trabajos_lista.html', {})
