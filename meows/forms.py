from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Meow

# =========================
# Formulario para crear y validar maullidos (publicaciones)
# =========================
class MeowForm(forms.ModelForm):
    class Meta:
        model = Meow  # Usa el modelo Meow
        fields = ['body']  # Solo se permite editar el campo 'body'
        widgets = {
            # Personalización del textarea para maullidos
            'body': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': 140,  # límite de caracteres
                'placeholder': '¿Qué estás maullando? (máx. 140 caracteres)',
                'class': 'form-control'
            }),
        }

    # Validación personalizada para el contenido del maullido
    def clean_body(self):
        data = self.cleaned_data['body'].strip()
        if not data:
            raise forms.ValidationError("No puedes publicar un maullido vacío.")
        if len(data) > 140:
            raise forms.ValidationError("Máximo 140 caracteres permitidos.")
        return data


# =========================
# Formulario de registro de usuarios personalizado
# =========================
class CustomUserCreationForm(UserCreationForm):
    # Campo para el nombre de usuario con placeholder y clase CSS
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={
            'placeholder': 'Escribe tu usuario',
            'class': 'form-control'
        })
    )
    # Campo para la contraseña con input de tipo password
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Escribe tu contraseña',
            'class': 'form-control'
        })
    )
    # Campo para confirmar la contraseña
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repite tu contraseña',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User  # Modelo de Django User
        fields = ["username", "password1", "password2"]  # Campos incluidos en el formulario
