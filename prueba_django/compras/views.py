from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contenido = {"nombre_sitio": "Pedidosasdasdasdasdasasd"}
    return render(request, "compras/index.html", contenido)


"""def index(request):
    return HttpResponse("Hola mundo!")
"""
