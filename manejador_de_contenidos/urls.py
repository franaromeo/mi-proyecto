"""mi_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_app.views import saludar_a, saludo, saludo_personalizado, calculo_imc, listar_cursos, listar_familiares, formulario_curso
from manejador_de_contenidos.views import mostrar_home, mostrar_profile, mostrar_messages

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludar/", saludo),
    path("saludar/persona/<nombre>", saludar_a),
    path("saludo-personalizado/", saludo_personalizado),
    path("imc/", calculo_imc),
    path("listar-cursos/", listar_cursos),
    path("listar-familiares/", listar_familiares),
    path("home/", mostrar_home),
    path("profile/", mostrar_profile),
    path("messages/", mostrar_messages),
    path("formulario/", formulario_curso)

]
