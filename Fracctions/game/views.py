from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
# Create your views here.

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)    

def index(request):
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('HOLA ' + nombre)

def bienvenida(request):
    letrero= "Bienvenida"
    return HttpResponse(letrero)

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    if(den1 == den2):
        numFin = num1 + num2
        denFin = den1
        resultado  = Fraccion(numFin, denFin)
    else:
        denFin = den1*den2
        num2 = den1*num2
        num1 = den2*num1
        numFin = num1+num2
        resultado = Fraccion(numFin, denFin)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
    content_type = "text/json-comment-filtred")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    if(den1 == den2):
        numFin = num1 - num2
        denFin = den1
        resultado  = Fraccion(numFin, denFin)
    else:
        denFin = den1*den2
        num2 = den1*num2
        num1 = den2*num1
        numFin = num1-num2
        resultado = Fraccion(numFin, denFin)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
    content_type = "text/json-comment-filtred")

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    numFin = num1*num2
    denFin = den1*den2
    resultado = Fraccion(numFin, denFin)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
    content_type = "text/json-comment-filtred")

#Cuando trae @ es una "anotación", un pedazo de código que se crea por cuenta propia
@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']
    num2 = body['numerador2']
    den2 = body['denominador2']
    numFin = num1*den2
    denFin = num2*den1
    resultado = Fraccion(numFin, denFin)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
    content_type = "text/json-comment-filtred")