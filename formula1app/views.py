from django.shortcuts import render

# Create your views here.

#<h7> <img src="{% static 'formula1app/img/lewis.jpg' %}" class="img-thumbnail" alt="..."> </h7>


def inicio(request):




    return render(request, "formula1app/inicio.html")
    