from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Los usuarios solo pueden registrarse como Lectores (el default del modelo)
        # Solo pedimos los campos necesarios para el registro.
        fields = ('username', 'email', 'first_name', 'last_name')