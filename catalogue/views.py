from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
# Create your views here.


def index(request):
    movies_amount = Movie.objects.all().count()
    actors_amount = Actor.objects.all().count()
    directors_amount = Director.objects.all().count()
    bronze_amount = Movie.objects.filter(subscription__movie=1).count()
    data = {'x': movies_amount, 'xx': actors_amount, 'xxxx': bronze_amount, 'xxx': directors_amount}

    return render(request, 'index.html', data)


# def allmovies(request):
#     return render(request, 'index.html')


class Movieslist(generic.ListView):
    model = Movie


# def movieinfo(request, id):
#     # return render(request, 'index.html')
#     movie = Movie.objects.get(id=id)
#     return HttpResponse(movie.title)

class Moviedetails(generic.DetailView):
    model = Movie

