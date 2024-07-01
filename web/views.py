from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Flan
from .forms import ContactFormForm

# Create your views here.
def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "views/index.html", {'flanes': flanes_publicos})

def acerca(request):
    return render(request, "views/about.html")

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    user_name = request.GET.get('name', 'cliente')
    return render(request, "views/welcome.html", {'user_name': user_name, 'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormForm()
    return render(request, 'views/contact.html', {'form': form})

def exito(request):
    return render(request, 'views/success.html')
