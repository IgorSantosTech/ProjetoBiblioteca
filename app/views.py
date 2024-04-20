from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.forms import LivroForm
from app.models import Livro
# Create your views here.
def home(request):
    livros = Livro.objects.all()
    return render(request, 'index.html', {'livros': livros})

def form(request):
    data = {}
    data['form'] = LivroForm()
    return render(request, 'form.html', data)

def create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivroForm()  # Criar um formulário vazio para requisições GET

    return render(request, 'form.html', {'form': form})

def view(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'view.html', {'livro': livro})

def edit(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(instance=livro)
    return render(request, 'form.html', {'form': form, 'livro': livro})

def update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'livro': livro})

def delete(request, pk):
    # Garante que somente requisições POST sejam processadas para evitar deletar com GET
    if request.method == 'POST':
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        messages.success(request, "Livro deletado com sucesso!")
        return redirect('home')
    else:
        messages.error(request, "Método inválido para esta operação.")
        return redirect('home')