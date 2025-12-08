from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    # ========================================
    # RUTAS HTML (Interfaz Web)
    # ========================================
    path('', views.home, name='home'),
    path('api-test/', views_api.api_test_view, name='api_test'),

    # URLs de Autores (HTML)
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor_detail'),
    path('autores/nuevo/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/eliminar/', views.AutorDeleteView.as_view(), name='autor_delete'),

    # URLs de Libros (HTML)
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro_detail'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete'),

    # ========================================
    # RUTAS API (RESTful Endpoints)
    # ========================================
    
    # Endpoints de Autores
    path('api/autores/', views_api.lista_autores, name='api_autores_lista'),
    path('api/autores/<int:pk>/', views_api.detalle_autor, name='api_autor_detalle'),
    
    # Endpoints de Libros
    path('api/libros/', views_api.lista_libros, name='api_libros_lista'),
    path('api/libros/<int:pk>/', views_api.detalle_libro, name='api_libro_detalle'),
]