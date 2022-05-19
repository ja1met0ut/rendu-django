from django.shortcuts import render
from .forms import SerieForm
from . import models
def index(request):
    liste = list(models.Serie.objects.all())
    return render(request, 'serie/index.html', {'liste': liste})

def ajout(request):
    if request.method == "POST":
        form = SerieForm(request)
        if form.is_valid():
            serie = form.save()
            return render(request,"/serie/affiche.html",{"serie" : serie})
        else:
            return render(request,"serie/ajout.html",{"form" : form})
    else:
        form = SerieForm()
        return render(request,"serie/ajout.html",{"form" : form})

def traitement(request):
    sform = SerieForm(request.POST)
    if sform.is_valid():
        serie = sform.save()
        return render(request,"/serie/affiche.html",{"serie" : serie})
    else:
        return render(request,"serie/ajout.html",{"form" : sform})

def affiche(request, id):
    serie = models.Serie.objects.get(pk=id)
    return render (request,"serie/affiche.html",{"serie" : serie})

def delete(request, id):
    serie = models.Serie.objects.get(pk=id)
    serie.delete()
    return HttpResponseRedirect("/serie/")

def update(request, id):
    serie = models.Serie.objects.get(pk=id)
    sform = SerieForm(serie.dico())
    return render(request, "serie/update.html", {"form": sform,"id":id})

def traitementupdate(request, id):
    sform = SerieForm(request.POST)
    if sform.is_valid():
        serie= sform.save(commit=False)
        serie.id = id;
        serie.save()
        return HttpResponseRedirect("/serie/")
    else:
        return render(request, "serie/update.html", {"form": sform, "id": id})
# Create your views here.
