from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    movies_amount = Movie.objects.all().count()
    actors_amount = Actor.objects.all().count()
    directors_amount = Director.objects.all().count()
    bronze_amount = Movie.objects.filter(subscription__movie=1).count()
    try:
        welcome_user_name = request.user.first_name
    except:
        welcome_user_name = 'Guest'
    data = {'x': movies_amount, 'xx': actors_amount, 'xxxx': bronze_amount, 'xxx': directors_amount, 'username': welcome_user_name}

    # создаём нового пользователя из-под программы
    # new_user = User.objects.create_user('user3', 'user3@user3.com', 'user3')
    # new_user.first_name = 'user3'
    # new_user.last_name = 'user3'
    # new_user.save()

    return render(request, 'index.html', data)


# def allmovies(request):
#     return render(request, 'index.html')


class Movieslist(generic.ListView):
    model = Movie
    paginate_by = 3     # выводить по Х фильмов на странице

# def movieinfo(request, id):
#     # return render(request, 'index.html')
#     movie = Movie.objects.get(id=id)
#     return HttpResponse(movie.title)

class Moviedetails(generic.DetailView):
    model = Movie

