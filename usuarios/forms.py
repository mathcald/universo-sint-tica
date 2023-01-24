from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nickname",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: mathcald"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=10, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label="Nome de Cadastro",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Matheus Caldas"
            }
        )
    )
    email = forms.EmailField(label="e-mail",
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: mathcald@unifesspa.edu.br"
            }
        )
    )
    senha1=forms.CharField(
        label="Senha",
        required=True,
        max_length=10, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )
    senha2=forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=10, 
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Confirme sua senha"
            }
        )
    )



