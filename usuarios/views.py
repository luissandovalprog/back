from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistroForm
from django.contrib import messages

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Mensaje de éxito antes de guardar
        messages.success(self.request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
        return super().form_valid(form)