from django.shortcuts import render
from .models import Autor, Livro
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def index(request):
    return render(request, 'biblioteca/index.html')


def inserirautor(request):
    if request.method == "POST":
        nome = request.POST['nome1']
        idade = request.POST['numero1']
        registro = Autor(nome=nome, idade=idade)
        registro.save()
        return HttpResponseRedirect(reverse('listarautores'))
    return render(request, 'biblioteca/inserirautor.html')


def inserirlivro(request):
    if request.method == "POST":
        titulo = request.POST['titulo1']
        autor = request.POST['autor1']
        objetoautor = Autor.objects.filter(nome=autor).first()
        resumo = request.POST['resumo1']
        registro = Livro(titulo=titulo, autor=objetoautor, resumo=resumo)
        registro.save()
        return HttpResponseRedirect(reverse('listarlivros'))
    return render(request, 'biblioteca/inserirlivro.html')


def login(request):
    return render(request, 'biblioteca/login.html')


def listarautores(request):
    registros = Autor.objects.all()
    return render(request, 'biblioteca/listarautores.html', {"registros": registros})


def listarlivros(request):
    registros = Livro.objects.all()
    return render(request, 'biblioteca/listarlivros.html', {"registros": registros})


def mostrarautor(request, id):
    objetoautor = Autor.objects.get(pk=id)
    return render(request, 'biblioteca/mostrarautor.html', {"autor": objetoautor})


def mostrarlivro(request, id):
    objetolivro = Livro.objects.get(pk=id)
    return render(request, 'biblioteca/mostrarlivro.html', {"livro": objetolivro})


def deletarautor(request, id):
    if request.method == "POST":
        autor = Autor.objects.get(pk=id)
        autor.delete()
        return HttpResponseRedirect(reverse('listarautores'))


def deletarlivros(request, id):
    if request.method == "POST":
        livro = Livro.objects.get(pk=id)
        livro.delete()
        return HttpResponseRedirect(reverse('listarlivros'))


def alterarautor(request, id):
    autor = get_object_or_404(Autor, pk=id)

    if request.method == "POST":
        nome = request.POST["nome2"]
        idade = request.POST["numero2"]
        autor.nome = nome
        autor.idade = idade
        autor.save()
        return redirect('listarautores')  # redireciona após salvar

    return render(request, 'biblioteca/alterarautor.html', {"autor": autor})
