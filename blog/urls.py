from django.urls import path
from blog import views



urlpatterns = [

    path('', views.bloguero, name="bloguero"),
    path('contenidos/<titulo>/', views.contenidos, name="contenidos"),

    


]
