from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.


class Pagar(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('pegar')


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('fechar pedido')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('detalhe')
