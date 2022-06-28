from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from . import models


class PerfilForm(ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)


class UserForm(ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data



