from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages

class BibliotecarioRequiredMixin(UserPassesTestMixin):
    """
    Mixin para Vistas Basadas en Clases.
    Verifica que el usuario esté autenticado y tenga el rol 'Bibliotecario'.
    """
    
    def test_func(self):
        # Verifica que el usuario esté logueado Y sea Bibliotecario
        return self.request.user.is_authenticated and self.request.user.rol == 'Bibliotecario'

    def handle_no_permission(self):
        """
        Redirige al home si el usuario no tiene permisos
        y muestra un mensaje de error.
        """
        messages.error(self.request, "Acceso denegado. Se requiere rol de Bibliotecario.")
        return redirect('home')