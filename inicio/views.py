from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.serializers import Serializer
from inicio.models import Producto, Categoria, Valorizacion
from inicio.forms import ProductoForm
from .forms import ValorizacionForm
from . import forms
from django.http import HttpResponseRedirect
from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from inicio import serializers

# Create your views here.
@api_view(['GET','POST'])
def producto_list(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def producto_detail(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(Serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def productoView(request):
    productos = Producto.objects.all()
    data = {'productos': list(productos.values('id','name','description','marca','categoria', 'price','stock', 'img_url'))}
    return JsonResponse(data)

def productoViewByID(request, producto_id):
    p = Producto.objects.get(id=producto_id)
    data = {'producto': {'id':p.id,'name':p.name,'description':p.description,'marca':p.marca,'categoria':str(p.categoria), 'price':p.price,'stock':p.stock, 'img_url':p.img_url}}
    return JsonResponse(data)

def productosViewByCategoria(request, categoria):
    productos = Producto.objects.filter(categoria=categoria)
    data = {'productos': list(productos.values('id','name','description','marca','categoria', 'price','stock', 'img_url'))}
    return JsonResponse(data)

def productosViewByMarca(request, marca):
    productos = Producto.objects.filter(marca=marca)
    data = {'productos': list(productos.values('id','name','description','marca','categoria', 'price','stock', 'img_url'))}
    return JsonResponse(data)

def valorizacionView(request):
    valorizaciones = Valorizacion.objects.all()
    data = {'valorizaciones': list(valorizaciones.values('producto','valoracion','comentario','autor'))}
    return JsonResponse(data)

def valorizacionViewByProductoID(request, producto_id):
    valorizaciones = Valorizacion.objects.filter(producto=producto_id)
    data = {'valorizaciones': list(valorizaciones.values('producto','valoracion','comentario','autor'))}
    return JsonResponse(data)


def valorizacionViewByAutor(request, autor):
    valorizaciones = Valorizacion.objects.filter(autor=autor)
    data = {'valorizaciones': list(valorizaciones.values('producto','valoracion','comentario','autor'))}
    return JsonResponse(data)

def listadoProductos(request):
    productos= Producto.objects.all()
    data = {'productos':productos}
    return render(request, 'productos.html', data)

def listaComputadoras(request):
    categoria = Categoria.objects.get(nombre="Computadoras y portátiles")
    productos = Producto.objects.filter(categoria=categoria)
    data = {'productos': productos}
    return render(request, 'productos.html', data)

def listaMoviles(request):
    categoria = Categoria.objects.get(nombre="Dispositivos móviles")
    productos = Producto.objects.filter(categoria=categoria)
    data = {'productos': productos}
    return render(request, 'productos.html', data)

def listaComponentes(request):
    categoria = Categoria.objects.get(nombre="Componentes")
    productos = Producto.objects.filter(categoria=categoria)
    data = {'productos': productos}
    return render(request, 'productos.html', data)

def listaAccesorios(request):
    categoria = Categoria.objects.get(nombre="Accesorios")
    productos = Producto.objects.filter(categoria=categoria)
    data = {'productos': productos}
    return render(request, 'productos.html', data)

def agregarProducto(request):
    form=forms.ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return listadoProductos(request)
    data = {'form' : form}
    return render(request, 'agregarProducto.html', data )

def quitarProducto(request, id):
    producto= Producto.objects.get(id=id)
    producto.delete()
    return redirect("/productos")

def cambiarProducto(request, id):
    producto= Producto.objects.get(id=id)
    form= ProductoForm(instance=producto)
    if request.method == 'POST':
        form= ProductoForm(request.POST, instance= producto)
        if form.is_valid():
            form.save()
        return listadoProductos(request)
    data = {'form': form}
    return render(request, 'agregarProducto.html', data)

def buscarProducto(request, id):
    producto= Producto.objects.get(id=id)
    data= {'productos': producto}
    return render(request, 'comunas.html',data)

def detallesProducto(request, id):
    producto = Producto.objects.get(id=id)
    valorizaciones = Valorizacion.objects.filter(producto = producto)
    
    if request.method == 'POST':
        form = ValorizacionForm(request.POST)
        if form.is_valid():
            valorizacion = form.save(commit=False)
            valorizacion.producto = producto
            valorizacion.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ValorizacionForm(initial={'producto': producto})
        data = {
        'producto': producto,
        'valorizaciones': valorizaciones,
        'form': form
        }
    return render(request, 'detallesProducto.html', data)

def agregarValorizacion(request):
    if request.method == 'POST':
        form = ValorizacionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ValorizacionForm()
    
    return render(request, 'detallesProducto.html', {'form': form})