from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import ContatoForm



# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    dados_pessoas = Blog.objects.all()
    return render(request, 'login.html', {'dados': dados_pessoas})

def basquete(request):
    return render(request, 'basquete.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco de dados
            return redirect('contato')  # Redireciona para a URL nomeada 'contato' ou outro destino desejado
    else:
        form = ContatoForm()  # Se o método não for POST, cria um formulário vazio

    return render(request, 'contato.html', {'form': form})
    
    #INFORMA COMO O FORMULARIO SERA CRIADO
    formulari = ContatoForm()
    return render(request, 'contato.html', {'form': formulario})


def fut(request):
    return render(request, 'fut.html')


