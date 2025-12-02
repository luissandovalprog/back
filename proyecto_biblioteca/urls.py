from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs de autenticación (Login y Logout)
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URLs de la app de usuarios (Registro)
    path('cuentas/', include('usuarios.urls')),

    # URLs de la app de catálogo (Home y CRUDs)
    path('', include('catalogo.urls')),
]