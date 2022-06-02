from random import choices
from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpRequest
from app_salud.models import Paciente, Medico, Obrasocial
from django.template import loader
from app_salud.forms import PacienteForm,MedicoForm,ObrasocialForm
from django.contrib import messages # PARA MENSAJES DE ALERTAS 
from django.db.models import Q # PARA QUE ME BUSQUE POR CUALQUIER CRITERIO
from django.core.paginator import Paginator #PARA LA PAGINACION DE LISTADOS

# Create your views here.

# REDIRIJO A LA PAGINA PRINCIPAL
def inicio(request):
    return render (request,"principal.html")

# PACIENTES
# ALTA DE NUEVO PACIENTE CON MENSAJE DE ALERTA
def form_paciente(request):
    if request.method == "POST":
        mi_formulario=PacienteForm(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            paciente=Paciente(apellido=datos['apellido'],nombre=datos['nombre'],dni=datos['dni'],fechaNac=datos['nacimiento']
                            ,obraSocial=datos['obra'],afiliado=datos['afiliado'],email=datos['email'])
            paciente.save()
            messages.success(request,"El paciente fue guardado con exito")
        return render (request, "paciente.html")
    return render (request, "paciente.html")

# LISTADO DE PACIENTES CON PAGINACION
def pacientes(request):
    paciente=Paciente.objects.all()
    page=request.GET.get("page",1)

    try: 
        paginator=Paginator(paciente,5)
        paciente=paginator.page(page)
    except:
        raise Http404
    dicc={
        "entity" : paciente,
        "paginator" : paginator 
    }
    plantilla=loader.get_template("lista_paciente.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

#BUSQUEDA DE PACIENTES POR CUALQUIER CRITERIO
def buscar_paciente(request):
    busqueda=request.GET.get("buscar")
    pacientes=""

    if busqueda:
        pacientes= Paciente.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(apellido__icontains = busqueda) |
            Q(dni__icontains = busqueda) |
            Q(obraSocial__icontains = busqueda)
        ).distinct()
    return render (request, "buscar_paciente.html", {"pacientes":pacientes})

#MEDICOS
#ALTA DE MEDICOS CON MENSAJE DE ALERTAS
def form_medico(request):
    if request.method == "POST":
        mi_formulario=MedicoForm(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            medico=Medico(profesional=datos['profesional'],mp=datos['mp'],especialidad=datos['especialidad'])
            medico.save()
            messages.success(request,"El profesional fue guardado con exito")
        return render (request, "medicos.html")
    return render (request, "medicos.html")

#LISTADO DE MEDICOS CON PAGINACION
def medicos(request):
    medico=Medico.objects.all()
    page=request.GET.get("page",1)

    try: 
        paginator=Paginator(medico,5)
        medico=paginator.page(page)
    except:
        raise Http404
    dicc={
        "entity" : medico,
        "paginator" : paginator 
    }
    plantilla=loader.get_template("lista_medico.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

#BUSQUEDA DE MEDICOS POR CUALQUIER CRITERIO
def buscar_medico(request):
    busqueda=request.GET.get("buscar")
    medicos=""

    if busqueda:
        medicos= Medico.objects.filter(
            Q(profesional__icontains = busqueda) |
            Q(mp__icontains = busqueda) |
            Q(especialidad__icontains = busqueda) 
        ).distinct()    
    
    return render (request, "buscar_medico.html", {"medicos":medicos})

#OBRA SOCIAL
#ALTA DE OBRAS SOCIALES CON MENSAJE ALERTA
def form_OS(request):
    if request.method == "POST":
        mi_formulario=ObrasocialForm(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            os=Obrasocial(nombre=datos['nombre'],direccion=datos['direccion'],email=datos['email'],cuit=datos['cuit'])
            os.save()
            messages.success(request,"La obra social fue guardada con exito")
        return render (request, "obrasocial.html")
    return render (request, "obrasocial.html")

# LISTADO DE OBRAS SOCIALES CON PAGINACION
def OS(request):
    OS=Obrasocial.objects.all()
    page=request.GET.get("page",1)

    try: 
        paginator=Paginator(OS,5)
        OS=paginator.page(page)
    except:
        raise Http404
    dicc={
        "entity" : OS,
        "paginator" : paginator 
    }
    plantilla=loader.get_template("lista_OS.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

#BUSQUEDA DE OBRAS SOCIALES POR CUALQUIER CRITERIO
def buscar_OS(request):
    busqueda=request.GET.get("buscar")
    OS=""

    if busqueda:
        OS= Obrasocial.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(cuit__icontains = busqueda) 
        ).distinct()    
    
    return render (request, "buscar_OS.html", {"Obras":OS})