"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core.views import *


urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('curso_administracao.html',curso_administracao),
    path('banco_de_dados.html',banco_de_dados),
    path('sistemas_de_informacao.html',sistemas_de_informacao),
    path('engenharia_da_computacao.html',engenharia_da_computacao),
    path('gestao_da_tecnologia_da_informacao.html',gestao_da_tecnologia_da_informacao),
    path('jogos_digitais.html',jogos_digitais),
    path('processos_gerenciais.html',processos_gerenciais),
    path('producao_multimidia.html',producao_multimidia),
    path('redes_de_computadores.html',redes_de_computadores),
]
