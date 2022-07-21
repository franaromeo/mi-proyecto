from django.shortcuts import render
from mi_app.forms import CursoFormulario

def mostrar_home(request):
    return render(request, "manejador_de_contenidos/home.html", {})

def mostrar_profile(request):
    return render(request, "manejador_de_contenidos/profile.html", {})

def mostrar_messages(request):
    return render(request, "manejador_de_contenidos/messages.html", {})