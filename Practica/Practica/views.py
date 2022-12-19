from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola a todos!")

def saludo_html(request):
    documento = """<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego!")

def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: {}</h1></body></html>""".format(fecha_actual)
    return HttpResponse(documento)

def calcular_edad(request,edad,agno):
    periodo=agno-datetime.datetime.now().year
    edad_futura=edad+periodo
    documento="<html><body><h2>En el año {} tendrás {} años".format(agno, edad_futura)
    return HttpResponse(documento)