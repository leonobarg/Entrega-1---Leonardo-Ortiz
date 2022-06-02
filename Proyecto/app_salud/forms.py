from django import forms

class PacienteForm (forms.Form):
    apellido=forms.CharField(max_length=40)
    nombre=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    nacimiento=forms.DateField()
    obra=forms.CharField(max_length=40)
    afiliado=forms.CharField(max_length=20)
    email=forms.EmailField()

class MedicoForm(forms.Form):
    profesional=forms.CharField(max_length=40)
    mp=forms.IntegerField()
    especialidad=forms.CharField(max_length=40)

class ObrasocialForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    direccion=forms.CharField(max_length=40)
    email=forms.EmailField()
    cuit=forms.IntegerField()