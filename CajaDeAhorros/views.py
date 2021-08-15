from django.shortcuts import render
from django.shortcuts import redirect
from .forms import FormCLiente
from .models import Cliente
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home_view(request):
    f = FormCLiente(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = Cliente()
            c.Nombre = datos.get("Nombre")
            c.Apellido = datos.get("Apellido")
            c.Cedula = datos.get("Cedula")
            c.Email = datos.get("Email")
            c.Telefono = datos.get("Telefono")
            if c.save() != True:
                print('Imprimo en pantalla y guardo data en BD')
                print(f.cleaned_data)
                return redirect(home_view)
    context = {
        "form":f,
    }

    return render(request, "home.html", context)

def about_view(request):
    return render(request, "about.html", {})
    
def contact_view(request,):
    return render(request, "contact.html", {})