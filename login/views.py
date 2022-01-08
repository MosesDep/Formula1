from django.shortcuts import render
from math import e
from django.shortcuts import redirect, render
from registro.models import usuarios
from django.contrib import messages
from tkinter import messagebox as MessageBox


def login(request):

    users=usuarios()


    if request.method =='POST':

        

        

        try:

            detallesusuario=usuarios.objects.get(email=request.POST.get("Email"),password=request.POST.get("contrasena") )

            

            request.session['email']=detallesusuario.email

            return render(request, "formula1app/base.html")




        except:


            messages.success(request, "Error Usuario Existente ")


                


             


    return render(request, "Login/login.html")