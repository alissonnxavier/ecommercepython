from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms


# Create your views here.


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.contexto = {
                'userform': forms.UserForm(data=self.request.POST or None, usuario=self.request.user, instance=self.request.user),
                'perfilform': forms.PerfilForm(data=self.request.POST or None)
            }

            self.renderizar = render(self.request, self.template_name, self.contexto)
        else:
            self.contexto = {'userform': forms.UserForm(data=self.request.POST or None), 'perfilform': forms.PerfilForm(data=self.request.POST or None)}

    def get(self, *args, **kwargs):
        return self.renderizar


class Criar(BasePerfil):
    def get(self, *args, **kwargs):
        return self.renderizar


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('atualizar')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('logout')
