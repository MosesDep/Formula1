from django.shortcuts import render
from stats.models import piloto, carrera,palmares, pole
from django.core.paginator import Paginator, EmptyPage


# Create your views here.



def stats(request):


    stats=piloto.objects.all()
    p=Paginator(piloto.objects.all(), 8)
    page=request.GET.get('page')
    line=p.get_page(page)

    context={

        'stats':stats,
        'line':line
    }



    

    return render(request, "stats/stats.html", context)




def carreras(request, nombre):

    siza=palmares.objects.filter(idnombre=nombre)

    stats=piloto.objects.filter(nombre=nombre)

    races=carrera.objects.filter(idnombre=nombre)

    p=Paginator(carrera.objects.filter(idnombre=nombre), 10)
    page=request.GET.get('page')
    line=p.get_page(page)

    context={

        'stats':stats,
        'line':line,
        'siza':siza,
        'races':races


    }



    return render(request, "stats/piloto.html", context)



def palmar(request,nombre):


    siza=palmares.objects.filter(idnombre=nombre)

    stats=piloto.objects.filter(nombre=nombre)

    poles=pole.objects.filter(idnombre=nombre)



    return render(request, "stats/poles.html", {"poles": poles,"stats": stats,"siza": siza })


