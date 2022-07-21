from django.shortcuts import render
from django.http import HttpResponse 
from mi_app.models import Curso, Familiar, Estudiante 
from mi_app.forms import CursoFormulario, CursoBusquedaFormulario, FamiliarFormulario, EstudianteFormulario

def saludo (request):
    
    return HttpResponse(f"Hola Mundo (fecha_hora_ahora)")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estás {nombre.capitalize()}")

def saludo_personalizado(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]
    return render(request, "mi_app/index.html", context)

def calculo_imc(request):
    context = {
        "imc":0
    }

    if request.GET:
        peso = float(request.GET["peso"])
        altura = float(request.GET["altura"])
        context["imc"] = peso / (altura **2)
    return render(request, "mi_app/index_2.html", context)

def listar_cursos(request):
    context = {}
    context["cursos"] = Curso.objects.all()
    return render(request, "mi_app/lista_cursos.html", context)

def listar_familiares(request):
    context = {}
    context["familiares"] = Familiar.objects.all()
    return render(request, "mi_app/listar_familiares.html", context)

def formulario_curso(request):

    if request.method == "POST":
        
        mi_formulario = CursoFormulario(request.POST)
        
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            curso = Curso (nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "mi_app/curso_formulario.html", {"mensaje":"Agregado con éxito!"})
    else:

        mi_formulario = CursoFormulario()
        return render(request, "mi_app/curso_formulario.html", {"mi_formulario":mi_formulario})

def formulario_busqueda(request):

    busqueda_formulario = CursoBusquedaFormulario()

    if request.GET:

        cursos = Curso.objects.filter(nombre=busqueda_formulario["criterio"]).all()
        return render(request, "mi_app/curso_busqueda.html", {"cursos":cursos})

    return render(request, "mi_app/curso_busqueda.html", {"busqueda_formulario":busqueda_formulario})

def formulario_familiar(request):

    if request.method == "POST":
        
        mi_formulario = FamiliarFormulario(request.POST)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            familiar = Familiar (nombre=informacion["nombre"], apellido=informacion["apellido"])
            familiar.save()
            return render(request, "mi_app/familiar_formulario.html", {"mensaje":"Agregado con éxito!"})
    else:

        mi_formulario = FamiliarFormulario()
        return render(request, "mi_app/familiar_formulario.html", {"mi_formulario":mi_formulario})

def formulario_estudiante(request):

    if request.method == "POST":
        
        mi_formulario = EstudianteFormulario(request.POST)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante (nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()
            return render(request, "mi_app/estudiante_formulario.html", {"mensaje":"Agregado con éxito!"})
    else:

        mi_formulario = EstudianteFormulario()
        return render(request, "mi_app/estudiante_formulario.html", {"mi_formulario":mi_formulario})