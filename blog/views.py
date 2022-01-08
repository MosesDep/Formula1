from django.shortcuts import render
from blog.models import blog, contenido




# Create your views here.


def bloguero(request):

    blogs=blog.objects.all()


    return render(request, "blog/blog.html", {"blogs": blogs})




def contenidos(request, titulo):


    texto=contenido.objects.filter(idtitulo=titulo)


    return render(request, "blog/contenidos.html", {"texto": texto})


