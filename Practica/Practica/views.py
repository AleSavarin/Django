from django.http import HttpResponse
import datetime
from django.template import Template, Context       # trabajar con los templates
from django.template import loader                  # para las plantillas
from django.template.loader import get_template
from django.shortcuts import render


'''
def saludo(request):Prac
    return HttpResponse("Hola a todos!")
'''
'''
def saludo(request):
    arch=open("G:/OneDrive - Instituto Nacional de Tecnología Industrial/CURSOS/Web-FrontEndPythonCABA/Codigo/Django/Practica\Practica/templates/plantilla.html")
    #arch=open("C:/Users/usuario/Desktop/Proyecto/Proyecto/templates/plantilla.html")
    nombre = "Alejandro"
    apellido = "Savarin"
    fecha = datetime.datetime.now()
    temas = ["Plantillas","Modelos","Formularios","Vistas"]       # Creo una lista para iterar

    plt=Template(arch.read())       # Interpreta el contenido del .html
    arch.close()                    # Cierra el archivo
    ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha,"temas_curso":temas})              # Define un contexto    
    documento=plt.render(ctx)       # Renderiza el contenido
    return HttpResponse(documento)
'''
def saludo(request):        # con loader, retorno un render()
    nombre = "Alejandro"
    apellido = "Savarin"
    fecha = datetime.datetime.now()
    temas = ["Plantillas","Modelos","Formularios","Vistas"]       # Creo una lista para iterar
    return render(request,'plantilla.html',{"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha,"temas_curso":temas})

# Practicar con herencia y vistas incrustadas
def curso(request):
    fecha = datetime.datetime.now()
    return render(request,"curso.html",{"now":fecha})

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