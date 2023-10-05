from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def index(request):     # index/home
    movies_amount = Movie.objects.all().count()
    actors_amount = Actor.objects.all().count()
    directors_amount = Director.objects.all().count()
    bronze_amount = Movie.objects.filter(subscription__movie=1).count()
    # if request.user.username:
    try:
        welcome_user_name = request.user.first_name
    # else:
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


class Movieslist(generic.ListView):     # для вывода списка фильмов
    model = Movie
    paginate_by = 3     # выводить по Х фильмов на странице

# def movieinfo(request, id):           # вариант реализации
#     # return render(request, 'index.html')
#     movie = Movie.objects.get(id=id)
#     return HttpResponse(movie.title)


class Moviedetails(generic.DetailView):     # для детального показа конкретного фильма
    model = Movie


def subscr(request):        # для страницы подписок
    try:
        welcome_user_name = request.user.first_name
    # else:
    except:
        welcome_user_name = 'Guest'

    subscriptions_all = Subscription.objects.all()

    data = {'subscriptions': subscriptions_all, 'username': welcome_user_name}
    return render(request, 'subscription.html', data)


def watcher(request, id1, id2, id3):
    print('movie id', 'subscr id', 'user id')
    print('id1', 'id2', 'id3')
    print(id1, id2, id3)
    subscription = None
    array_subscription = ['bronze', 'silver', 'gold']
    array_user_tier = ['bronze tier', 'silver tier', 'gold tier']
    if id3 != 0:
        subscription = User.objects.get(id=id3)     # нашли юзера
        subscription = subscription.groups.all()    # нашли его подписки
        subscription = subscription[0].id           # нашли id подписки
    else:
        if id3 == 0:                                # если гость, даём ему базовую подписку
            subscription = 1
    if subscription >= id2:                     # сравнение прав пользователя и прав фильма
        print('ok')
    else:
        print('Not Ok')
    return render(request, 'index.html')


class Actorslist(generic.ListView):
    model = Actor


class Actordetails(generic.DetailView):
    model = Actor


class Directorslist(generic.ListView):
    model = Director


class Directordetails(generic.DetailView):
    model = Director