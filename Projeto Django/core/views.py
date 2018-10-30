from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render (request,"index.html")

def home(request):
    return render (request,"index.html") 

def curso_administracao(request):
    return render (request,"curso_administracao.html") 

def banco_de_dados(request):
    return render (request,"banco_de_dados.html") 

def sistemas_de_informacao(request):
    return render (request," sistema_de_informacao.html")     

def engenharia_da_computacao(request):
    return render (request,"engenharia_da_computacao.html") 

def gestao_da_tecnologia_da_informacao(request):
    return render (request,"gestao_da_tecnologia_da_informacao.html") 

def jogos_digitais(request):
    return render (request,"jogos_digitais.html")

def processos_gerenciais(request):
    return render (request,"processos_gerenciais.html") 

def curso_producao_multimidia(request):
    return render (request,"curso_producao_multimidia.html") 

def curso_redes_de_computadores(request):
    return render (request,"curso_redes_de_computadores.html") 