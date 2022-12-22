from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto

# FORMULARIOS


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["prd"]:
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje = "Texto de búsqueda demasiado largo"
            return HttpResponse(mensaje)
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})
    else:
        mensaje = "No has introducido ningún dato"
        return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            # Realizar operación con los datos aquí e incluir gracias.html
            return render(request, "gracias.html",{"respuestaFormulario": infForm})
    else:
        miFormulario = FormularioContacto()
        return render(request, "formulario_contacto.html", {"form": miFormulario})
