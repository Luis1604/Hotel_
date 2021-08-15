from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    Nombre=models.CharField(max_length=30,blank=False)
    Apellido=models.CharField(max_length=30,blank=False,default='')
    Cedula=models.CharField(max_length=30,blank=False,default='')
    Email=models.EmailField(max_length=30,blank=False,default='')
    Telefono=models.CharField(max_length=30,blank=False,default='')

def __str__(self):
    return "%s %s" % (self.Nombre, self.Apellido)

class Cuenta(models.Model):
    
    idCliente=models.ForeignKey(Cliente(), on_delete=models.CASCADE, default="")
    Numero_de_Cuenta=models.CharField(max_length=30, blank=False)
    Saldo=models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    Tipo=models.IntegerField(choices=((1, ("Ahorro")),(2, ("Corriente"))), default=1)
    Propietario=models.CharField(max_length=30, blank=False, unique=True, null=True)

def __str__(self):
    return self.Propietario

class Transferencia(models.Model):
    
    idCuenta=models.ForeignKey(Cuenta(), on_delete=models.CASCADE,default="")
    Numero_de_Cuenta=models.CharField(max_length=30,blank=False)
    Tipo=models.IntegerField(choices=((1, ("Deposito")),(2, ("Retiro"))), default=1)
    Fecha=models.DateField(blank=False)
    Monto=models.DecimalField(max_digits=5,decimal_places=2,blank=False)

def __str__(self):
    return self.Fecha

class Prestamo(models.Model):
    
    idCuenta=models.ForeignKey(Cuenta(), on_delete=models.CASCADE)
    Monto=models.DecimalField(max_digits=5,decimal_places=2,blank=False)
    Interes=models.CharField(max_length=30,blank=False)
    Plazo=models.CharField(max_length=30,blank=False)

def __str__(self):
    return self.Fecha