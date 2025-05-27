from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'biblioteca/index.html')


def inserirautor(request):
    return render(request, 'biblioteca/inserirautor.html')


def inserirlivro(request):
    return render(request, 'biblioteca/inserirlivro.html')


def login(request):
    return render(request, 'biblioteca/login.html')


def listarautores(request):
    return render(request, 'biblioteca/listaauroes.html')


def listarlivros(request):
    return render(request, 'biblioteca/listarlivros.html')
