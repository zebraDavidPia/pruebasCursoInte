from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto
# Create your views here.


def index(request):
    productos = Producto.objects.all()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )
def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request,'detalle.html',context={'producto': producto})

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productos:index'))
    else:
        form = ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form': form}
    )

def editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productos:detalle', args=[producto_id]))
    else:
        form = ProductoForm(instance=producto)
    return render(
        request,
        'producto_form.html',
        {'form': form, 'producto': producto}
    )

def eliminar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return HttpResponseRedirect(reverse('productos:index'))
    return render(request, 'producto_confirmar_eliminar.html', {'producto': producto})