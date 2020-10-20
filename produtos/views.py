from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


@login_required
def lista_produtos(request):
    lista = Product.objects.all()
    return render(request, 'lista_produtos.html', {'lista': lista})


@login_required
def novo_produto(request):
    # Cria um formulário vazio ou preenchido com os dados do POST
    # Se houver imagens enviadas no formulário, são salvas 'requests.FILES'
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'product_form.html', {'form': form})


@login_required
def edita_produto(request, id):
    produto = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'product_form.html', {'form': form})


@login_required
def deleta_produto(request, id):
    produto = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista')
    return render(request, 'confirma_delete.html', {'produto': produto})
