from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class FamiliarFormulario(forms.Form):

    nombre = forms.CharField()
    edad = forms.IntegerField()

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()