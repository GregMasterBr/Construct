from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators import has_permission_decorator
from .models import Categoria, Produto, Imagem
from django.urls import reverse
from django.contrib import auth
#Django Messages - definida lá no settings - MESSAGES_TAG
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

def adicionar_produto(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render (request, 'adicionar_produto.html', {'categorias':categorias} )
    elif request.method == "POST":
        produto = request.POST.get("produto")
        categoria = request.POST.get("categoria")
        quantidade = request.POST.get("quantidade")
        preco_compra = request.POST.get("preco_compra")
        preco_venda = request.POST.get("preco_venda")
        imagens = request.FILES.getlist("imagens")
        produto = Produto(nome=produto,categoria=categoria, quantidade=quantidade, preco_compra=preco_compra, preco_venda=preco_venda )

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.add_message(request, constants.ERROR, 'Produto excluído com sucesso!')
    return redirect(reverse('adicionar_produto'))