from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Meow

# === Formulario para maullidos ===
class MeowForm(forms.ModelForm):
    class Meta:
        model = Meow
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': 140,
                'placeholder': '¿Qué estás maullando? (máx. 140 caracteres)',
                'class': 'form-control'
            }),
        }

    def clean_body(self):
        data = self.cleaned_data['body'].strip()
        if not data:
            raise forms.ValidationError("No puedes publicar un maullido vacío.")
        if len(data) > 140:
            raise forms.ValidationError("Máximo 140 caracteres permitidos.")
        return data


# === Formulario de registro personalizado ===
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            'placeholder': 'Escribe tu usuario',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Escribe tu contraseña',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite tu contraseña',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
