from django.shortcuts import render
from grupo.models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'grupo/index.html', {"cards": pessoas})

def imagem(request):
    return render(request, 'grupo/imagem.html')

def cadastro(request):
    return render(request, 'grupo/cadastro.html')
