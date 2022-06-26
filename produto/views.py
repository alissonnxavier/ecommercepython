from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from django.views.generic import DeleteView, DetailView
from . import models


# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 1


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('adicionar ao carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('remover carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('finalizar')
