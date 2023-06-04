from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Producto, Categoria, Valorizacion
from inicio.forms import ProductoForm
from .forms import ValorizacionForm
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.

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