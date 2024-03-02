from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos


# Create your views here.


def index(request):
    return render(request, 'index.html')

def produtos(request):
    return render(request, 'produtos.html')

def listar(request):
    lista_clientes = Produtos.objects.all()
    return render(request, 'listar.html', {'lista': lista_clientes})