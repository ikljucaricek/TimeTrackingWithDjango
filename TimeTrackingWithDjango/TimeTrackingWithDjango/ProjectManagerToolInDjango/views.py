from django.http import HttpResponse

from django.shortcuts import render_to_response, RequestContext, render

from TimeTrackingWithDjango.ProjectManagerToolInDjango import models
from django.db.models import Q
from itertools import chain



def index(request):
    return render("index.html")

def osobaprojekt(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        osobaprojekt_sve = models.OsobaProjekt.objects.all()
        for qry in q.split():
            osobaprojekt_sve = osobaprojekt_sve.filter(Q(id_projekt = qry)|Q(id_osoba = qry))
    else:
        osobaprojekt_sve = models.OsobaProjekt.objects.all()
    ctx = { 'oNp':osobaprojekt_sve }
    return render_to_response("osobaprojekt.html", ctx)

def osobe(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        query = models.Osoba.objects.all()
        for qry in q.split():
            query = query.filter(Q(ime_osoba = qry) | Q(prezime_osoba = qry))
    else:
        query = models.Osoba.objects.all()
    ctx = {'osobe' : query}
    return render_to_response("osobe.html", ctx)


def projekti(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        projekti_svi = models.Projekt.objects.filter(naziv_projekt = q)
    else:
        projekti_svi = models.Projekt.objects.all()
    ctx = { 'projekti' : projekti_svi }
    return render_to_response("projekti.html", ctx)