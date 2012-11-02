# Create your views here.

#Modelos de la aplicacion actual
from audith.models import *

#Modulos de Django
from django.contrib.humanize.templatetags.humanize import *
from django.utils.numberformat import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Count

#Modulos de python
import simplejson as json
import pandas
import numpy as np
import datetime
import decimal

def mezcla_institucion(request):
        #Template que se utilizara
    template = 'mezcla_institucion.html'
        #Convertir resultado en un DataFrame
    registros = Generales.objects.prefetch_related('onco').all()
    data = pandas.DataFrame.from_records(registros.values('folio','institucion').annotate(Total=Count('id_unico')))
        #Crear la pivot_table 'Tabla de referencias cruzadas'
    pvt = pandas.pivot_table(data, values='Total', rows=['institucion'], cols=['folio'], aggfunc=np.sum)
        #Convertir el recultado en un diccionario
    elementos = pvt.to_dict()
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
        #Enviar parametros al 'render_to_response'
    return render_to_response(template,lista)

def medicos_residentes(request):
        #Template que se utilizara
    template = 'medicos_residentes.html'
        #Obtiene los valores mediante una vista con varios modelos
    elementos = Generales.objects.all().prefetch_related('onco').filter(tema_cod__exact=1).filter(tipo_medico__exact='RESIDENTE').filter(medico_adscrito__isnull=True).order_by('fecha','folio')
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)

def dx_1(request):
        #Template que se utilizara
    template = 'vacios.html'
        #Obtiene los valores mediante una vista con varios modelos
    elementos = Generales.objects.all().prefetch_related('onco').filter(tema_cod__exact=1).filter(onco__dx_1__isnull=True)
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)

def dx_2(request):
        #Template que se utilizara
    template = 'vacios.html'
        #Obtiene los valores mediante una vista con varios modelos
    elementos = Generales.objects.all().prefetch_related('onco').filter(tema_cod__exact=1).filter(onco__dx_2__isnull=True)
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)

def numero_pacientes(request):
        #Template que se utilizara
    template = 'vacios.html'
        #Obtiene los valores mediante una vista con varios modelos
    elementos = Generales.objects.all().prefetch_related('onco').filter(tema_cod__exact=1).filter(num_pacientes__isnull=True)
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)

def folio_paciente(request):
        #Template que se utilizara
    template = 'vacios.html'
        #Obtiene los valores mediante una vista con varios modelos
    elementos = Generales.objects.all().prefetch_related('onco').filter(tema_cod__exact=1).filter(onco__n__isnull=True)
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)

def esquemas(request):
        #Template que se utilizara
    template = 'vacios.html'
        #Obtiene los valores mediante una vista con varios modelos
    elementos = OncoCasos.objects.all().filter(tema_cod__exact=1).filter(esquema_tx__contains='CAPECITABINA')
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)

def inicio(request):
        #Template que se utilizara
    template = 'inicio.html'
        #Obtiene los valores mediante una vista con varios modelos
    institucion = Generales.objects.values('institucion','sector').annotate(Total=Count('id_unico')).order_by('-Total')
    elementos = Generales.objects.values('medico_cod','medico_des','tipo_medico').prefetch_related('onco').annotate(Total=Count('id_unico')).order_by('medico_des')
        #Asignar resultados a la lista para 'render_to_response'
    lista = {'lista':elementos}
    return render_to_response(template,lista)