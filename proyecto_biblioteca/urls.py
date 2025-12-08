from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),
    
    # ========================================
    # ENDPOINTS JWT - Autenticación API
    # ========================================
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # ========================================
    # URLs de autenticación HTML (Login y Logout)
    # ========================================
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URLs de la app de usuarios (Registro)
    path('cuentas/', include('usuarios.urls')),

    # URLs de la app de catálogo (Home, CRUDs HTML y API)
    # IMPORTANTE: Esto debe ir AL FINAL
    path('', include('catalogo.urls')),
]