from django import forms
from .models import Cuenta, Cliente, Transferencia, Prestamo

class FormCLiente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields=["Nombre","Apellido","Cedula","Email","Telefono"]
