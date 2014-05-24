from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, render, redirect

from TimeTrackingWithDjango.ProjectManagerToolInDjango import models
from django.db.models import Q

from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext



def index(request):
    return render(request, "index.html")

#@csrf_protect
def osobaprojekt(request):
    if request.method == 'POST':
        projekt = request.POST.get('id_projekt')
        osoba = request.POST.get('id_osoba')
        br_sati = request.POST.get('br_sati')
        datum = request.POST.get('datum')
        offer = models.OsobaProjekt.objects.create(id_projekt_id=projekt, id_osoba_id=osoba, br_sati=br_sati, datum=datum)
        osobaprojekt_sve = models.OsobaProjekt.objects.all()
        osobe = models.Osoba.objects.all()
        projekti = models.Projekt.objects.all()
        return redirect('index')
    else:
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            osobaprojekt_sve = models.OsobaProjekt.objects.all()
            osobe = models.Osoba.objects.all()
            projekti = models.Projekt.objects.all()
            for qry in q.split():
                osobaprojekt_sve = osobaprojekt_sve.filter(Q(id_projekt = qry)|Q(id_osoba = qry))
        else:
            osobaprojekt_sve = models.OsobaProjekt.objects.all()
            osobe = models.Osoba.objects.all()
            projekti = models.Projekt.objects.all()
    ctx = { 'oNp':osobaprojekt_sve, 'osobe' :osobe, 'projekti':projekti}
    return render(request, 'osobaprojekt.html', ctx)

def osobe(request):
    if request.method == 'POST':
        ime_osoba = request.POST.get('ime_osoba')
        prezime_osoba = request.POST.get('prezime_osoba')
        models.Osoba.objects.create(ime_osoba=ime_osoba, prezime_osoba=prezime_osoba)
        query = models.Osoba.objects.all()
        return redirect('index')
    else:
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            query = models.Osoba.objects.all()
            for qry in q.split():
                query = query.filter(Q(ime_osoba = qry) | Q(prezime_osoba = qry))
        else:
            query = models.Osoba.objects.all()
    ctx = {'osobe' : query}
    return render(request, "osobe.html", ctx)


def projekti(request):
    if request.method == 'POST':
        naziv_projekt = request.POST.get('naziv_projekt')
        aktivan = request.POST.get('aktivan')
        datum_pocetak = request.POST.get('datum_pocetak')
        datum_zavrsetak = request.POST.get('datum_zavrsetak')
        models.Projekt.objects.create(naziv_projekt=naziv_projekt, aktivan=aktivan, datum_pocetak=datum_pocetak, datum_zavrsetak=datum_zavrsetak)
        projekti_svi = models.Projekt.objects.all()
        return redirect('index')
    else:
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            projekti_svi = models.Projekt.objects.filter(naziv_projekt = q)
        else:
            projekti_svi = models.Projekt.objects.all()
    ctx = { 'projekti' : projekti_svi }
    return render(request, "projekti.html", ctx)

def brisanje_osobe(request, id):
    models.Osoba.objects.get(id_osoba=id).delete()
    return redirect('index')

def brisanje_projekta(request, id):
    models.Projekt.objects.get(id_projekt=id).delete()
    return redirect('index')