from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import UserBlog

class formulario(forms.ModelForm):

    class Meta:
        model = FormServicos
        fields = ['nome', 'numero', 'servico', 'email', 'data', 'detalhes']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'detalhes': forms.Textarea(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'DD/MM/AAAA'}),
        }

class UserBlogCreationForm(UserCreationForm):
    cpf = forms.CharField(max_length=11, required=True, help_text="Digite seu CPF sem pontos ou traços.")

    class Meta:
        model = UserBlog
        fields = ('username', 'cpf', 'email', 'password1', 'password2')

class Procurarcarro(forms.Form):
    nome = forms.CharField(required=False, label='Buscar carro',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do carro'
        })
    )