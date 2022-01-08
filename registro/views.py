from django.shortcuts import render, redirect
from registro.models import usuarios
from django.contrib import messages


# Create your views here.




def registro(request):


    users=usuarios()


    if request.method=='POST':

            
        
        email=request.POST.get("Email")
        nombre=request.POST.get("name")
        apellido=request.POST.get("last")
        nacimiento=request.POST.get("fecha")
        foto=request.POST.get("foton")
        origen=request.POST.get("origen")
        genero=request.POST.get("genero")
        password=request.POST.get("contra")


        verificar=usuarios.objects.filter(email=request.POST.get("Email"))

        if verificar:
            messages.success(request, "Error Usuario Existente ")
             
        else:
            users = usuarios(email,nombre,apellido,nacimiento,foto, origen, genero, password)
            users.save()
            return redirect("login")




        


        





    return render(request, "registro/registro.html")


 
             


 