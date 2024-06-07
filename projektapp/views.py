from django.shortcuts import render
from .models import Čtenář, Půjčka, Knihovna, Knihovník, Rezervace

def index(request):
    # Získání dat z vašich modelů
    čtenáři = Čtenář.objects.all()
    půjčky = Půjčka.objects.all()
    knihovny = Knihovna.objects.all()
    knihovníci = Knihovník.objects.all()
    rezervace = Rezervace.objects.all()

    # Předání dat do šablony index.html
    return render(request, 'index.html', {
        'čtenáři': čtenáři,
        'půjčky': půjčky,
        'knihovny': knihovny,
        'knihovníci': knihovníci,
        'rezervace': rezervace,
    })
