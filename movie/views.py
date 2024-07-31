from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.

def home(request):
    # return HttpResponse("<h1>Welcome to home page</h1>")
    # return render(request, "home.html")
    # return render(request, "home.html", {"name":"Sebastián Uribe"})

    searchTerm = request.GET.get("searchMovie")
    if searchTerm:
        movies = Movie.objects.filter(title__contains=searchTerm)
    else:
        movies = Movie.objects.all()
    
    return render(request,"home.html", {"searchTerm":searchTerm, "movies": movies})

def about(request):
    # return HttpResponse("<h1>Welcome to About page</h1>")
    return render(request, "about.html")

