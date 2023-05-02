from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Cargo, Persona

# Create your views here.
def index(request):
    try:
        personas = get_list_or_404(Persona)
        return render(request, 'index.html', {
            'personas': personas
        })
    except:
        return render(request, 'index.html')

def detalles(request, id_persona):
    persona = get_object_or_404(Persona.objects.filter(id=id_persona))
    return render(request, 'detalles.html', {
        'persona': persona
    })