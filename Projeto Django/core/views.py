from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   
   
    return render (request,"index.html")

def curso_administracao(request):
   
   
    return render (request,"curso_administracao.html") 
    