from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render (request,"index.html")

def login(request):
    return render (request,"login.html")

def home(request):
    return render (request,"index.html") 

def curso_administracao(request):
    return render (request,"curso_administracao.html") 

def curso_banco_de_dados(request):
    return render (request,"curso_banco_de_dados.html") 

def curso_sistemas_de_informacao(request):
    return render (request,"curso_sistemas_de_informacao.html")     

def curso_engenharia_da_computacao(request):
    return render (request,"curso_engenharia_da_computacao.html") 

def curso_gestao_da_tecnologia_da_informacao(request):
    return render (request,"curso_gestao_da_tecnologia_da_informacao.html") 

def curso_jogos_digitais(request):
    return render (request,"curso_jogos_digitais.html")

def curso_processos_gerenciais(request):
    return render (request,"curso_processos_gerenciais.html") 

def curso_producao_multimidia(request):
    return render (request,"curso_producao_multimidia.html") 

def curso_redes_de_computadores(request):
    return render (request,"curso_redes_de_computadores.html") 

def curso_analise_e_desenvolvimento_de_sistemas(request):
    return render (request,"curso_analise_e_desenvolvimento_de_sistemas.html")

