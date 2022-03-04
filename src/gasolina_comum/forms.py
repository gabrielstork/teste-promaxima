from django import forms
from . import models


class GasolinaComumForm(forms.ModelForm):
    """
    Formulário para adicionar e editar objetos ao banco de dados.
    """
    class Meta:
        model = models.GasolinaComum
        exclude = ('raspagem',)

        widgets = {
            'tipo': forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-light font-size-md custom-input', 'id': 'tipo-input'}),
            'valor_unitario': forms.TextInput(attrs={'type': 'number', 'class': 'form-control text-light font-size-md custom-input', 'id': 'valor-unitario-input', 'step': '0.001'}),
            'valor_ultima_venda': forms.TextInput(attrs={'type': 'number', 'class': 'form-control text-light font-size-md custom-input', 'id': 'valor-ultima-venda-input', 'step': '0.001'}),
            'tempo_ultima_venda': forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-light font-size-md custom-input', 'id': 'tempo-ultima-venda-input'}),
            'contribuinte': forms.TextInput(attrs={'type': 'text', 'class': 'form-control text-light font-size-md custom-input', 'id': 'contribuinte-input'}),
            'codigo': forms.TextInput(attrs={'type': 'number', 'class': 'form-control text-light font-size-md custom-input', 'id': 'codigo-input'}),
        }