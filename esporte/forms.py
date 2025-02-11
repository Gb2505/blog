from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    #Classe padrão que define quais campos iremos usar
    class Meta:
        #Informa o modelo
        model = Contato

        #Informa os campos
        fields = ['nome', 'email', 'mensagem']

        #Define como as labels apareceram no formulario
        labels = {
            'nome': 'Nome completo:',
            'email': 'Informe seu email:',
            'mensagem': 'Digite sua mensagem:'
        }

        #Utilizar css
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite seu nome"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Digite seu e-mail"}),
            "mensagem": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Digite sua mensagem"}),
    }