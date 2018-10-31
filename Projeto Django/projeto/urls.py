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
    path('index.html',home),
    path('curso_administracao.html',curso_administracao),
    path('curso_banco_de_dados.html',curso_banco_de_dados),
    path('curso_sistemas_de_informacao.html',curso_sistemas_de_informacao),
    path('curso_engenharia_da_computacao.html',curso_engenharia_da_computacao),
    path('curso_gestao_da_tecnologia_da_informacao.html',curso_gestao_da_tecnologia_da_informacao),
    path('curso_jogos_digitais.html',curso_jogos_digitais),
    path('curso_processos_gerenciais.html',curso_processos_gerenciais),
    path('curso_producao_multimidia.html',curso_producao_multimidia),
    path('curso_redes_de_computadores.html',curso_redes_de_computadores),
#   path('curso_analise_e_desenvolvimento_de_sistemas.html',curso_analise_e_desenvolvimento_de_sistemas),
]
