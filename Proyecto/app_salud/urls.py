from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("alta_paciente", views.form_paciente, name="alta_paciente"),
    path("lista_pac", views.pacientes, name="lista_pac"),
    path("buscar_paciente", views.buscar_paciente, name="buscar_pac"),
    path("alta_medico", views.form_medico, name="alta_medico"),
    path("lista_medico", views.medicos, name="lista_medico"),
    path("buscar_medico", views.buscar_medico, name="buscar_medico"),
    path("alta_OS", views.form_OS, name="alta_OS"),
    path("lista_OS", views.OS, name="lista_OS"),
    path("buscar_OS", views.buscar_OS, name="buscar_OS"),
]
