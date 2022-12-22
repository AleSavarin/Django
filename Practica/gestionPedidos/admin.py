from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono",)         # indica que campos mostrar
    search_fields=("nombre","telefono",)                    # sobre que campos se pueden hacer búsquedas
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)                                # que campo filtrar

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")                     
    list_filter=("fecha",) 
    date_hierarchy="fecha"

admin.site.register(Clientes,ClientesAdmin) 
admin.site.register(Articulos,ArticulosAdmin) 
admin.site.register(Pedidos,PedidosAdmin) 
