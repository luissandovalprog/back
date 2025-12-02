from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Autor, Libro
from .forms import AutorForm, LibroForm
from usuarios.decorators import BibliotecarioRequiredMixin # Importamos el Mixin de roles

# --- Vista Home ---
def home(request):
    return render(request, 'home.html')


# --- CRUD de Autores ---

class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name = 'catalogo/autor_list.html'
    context_object_name = 'autores'

class AutorDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = 'catalogo/autor_detail.html'

class AutorCreateView(LoginRequiredMixin, BibliotecarioRequiredMixin, SuccessMessageMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalogo/autor_form.html'
    success_url = reverse_lazy('autor_list')
    success_message = "Autor creado exitosamente."

class AutorUpdateView(LoginRequiredMixin, BibliotecarioRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalogo/autor_form.html'
    success_url = reverse_lazy('autor_list')
    success_message = "Autor actualizado exitosamente."

class AutorDeleteView(LoginRequiredMixin, BibliotecarioRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Autor
    template_name = 'catalogo/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')
    success_message = "Autor eliminado exitosamente."


# --- CRUD de Libros ---

class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'catalogo/libro_list.html'
    context_object_name = 'libros'

class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = 'catalogo/libro_detail.html'

class LibroCreateView(LoginRequiredMixin, BibliotecarioRequiredMixin, SuccessMessageMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'catalogo/libro_form.html'
    success_url = reverse_lazy('libro_list')
    success_message = "Libro creado exitosamente."

class LibroUpdateView(LoginRequiredMixin, BibliotecarioRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'catalogo/libro_form.html'
    success_url = reverse_lazy('libro_list')
    success_message = "Libro actualizado exitosamente."

class LibroDeleteView(LoginRequiredMixin, BibliotecarioRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Libro
    template_name = 'catalogo/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')
    success_message = "Libro eliminado exitosamente."