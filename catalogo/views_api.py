from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer
import traceback


# ========================================
# VISTA PARA FRONTEND DE PRUEBA
# ========================================

def api_test_view(request):
    """
    Vista que sirve la interfaz HTML para probar la API
    """
    return render(request, 'api_test.html')


# ========================================
# API ENDPOINTS PARA AUTOR
# ========================================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_autores(request):
    """
    GET: Lista todos los autores
    POST: Crea un nuevo autor
    """
    try:
        if request.method == 'GET':
            autores = Autor.objects.all()
            serializer = AutorSerializer(autores, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            serializer = AutorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {'error': str(e), 'traceback': traceback.format_exc()},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_autor(request, pk):
    """
    GET: Obtiene un autor específico
    PUT: Actualiza un autor existente
    DELETE: Elimina un autor
    """
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(
            {'error': 'Autor no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        autor.delete()
        return Response(
            {'mensaje': 'Autor eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )


# ========================================
# API ENDPOINTS PARA LIBRO
# ========================================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_libros(request):
    """
    GET: Lista todos los libros
    POST: Crea un nuevo libro
    """
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_libro(request, pk):
    """
    GET: Obtiene un libro específico
    PUT: Actualiza un libro existente
    DELETE: Elimina un libro
    """
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response(
            {'error': 'Libro no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        libro.delete()
        return Response(
            {'mensaje': 'Libro eliminado exitosamente'},
            status=status.HTTP_204_NO_CONTENT
        )