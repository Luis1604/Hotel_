from django.contrib import admin
from .models import Cuenta, Cliente, Transferencia, Prestamo

class AdminCuenta(admin.ModelAdmin):
    list_display = ["__str__","Numero_de_Cuenta","Saldo","Propietario","Tipo"]
    class Meta(object):
        model = Cuenta

admin.site.register(Cuenta,AdminCuenta)

class AdminCliente(admin.ModelAdmin):
    list_display = ["__str__","Nombre","Apellido","Cedula","Email","Telefono"]
    class Meta(object):
        model = Cliente

admin.site.register(Cliente,AdminCliente)

class AdminTransferencia(admin.ModelAdmin):
    list_display = ["__str__","Numero_de_Cuenta","Tipo","Fecha","Monto"]
    class Meta(object):
        model = Transferencia

admin.site.register(Transferencia,AdminTransferencia)

class AdminPrestamo(admin.ModelAdmin):
    list_display = ["__str__","Monto","Interes","Plazo"]
    class Meta(object):
        model = Prestamo

admin.site.register(Prestamo,AdminPrestamo)