from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from catalogue import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
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
    paginate_by = 5     # выводить по Х фильмов на странице

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


def watcher(request, id1, id2, id3):        # для просмотра фильма
    print('movie id', 'subscr id', 'user id')
    print('id1', 'id2', 'id3')
    print(id1, id2, id3)
    subscription = None
    array_subscription = ['bronze', 'silver', 'gold']
    array_user_tier = ['bronze tier', 'silver tier', 'gold tier']
    if id3 != 0:        # проверка для не-гостя
        subscription = User.objects.get(id=id3)     # нашли юзера
        subscription = subscription.groups.all()    # нашли его подписки
        subscription = subscription[0].id           # нашли id подписки
    else:       # если гость
        if id3 == 0:                                # если гость, даём ему базовую подписку
            subscription = 1
    if subscription >= id2:                     # сравнение прав пользователя и прав фильма
        print('ok')
        permission = True
    else:
        print('Not Ok')
        permission = False
    movie_title = Movie.objects.get(id=id1).title
    subscriptiontier = Group.objects.get(id=subscription).name
    subscriptionmovie = Subscription.objects.get(id=id2).subscription_type

    try:
        welcome_user_name = request.user.first_name
    except:
        welcome_user_name = 'Guest'

    data = {'movie': movie_title, 'subscriptiontier': subscriptiontier, 'subscriptionmovie': subscriptionmovie, 'permission': permission, 'username': welcome_user_name}
    return render(request, 'watch.html', data)


class Actorslist(generic.ListView):     # для вывода актёров
    model = Actor
    paginate_by = 5


class Actordetails(generic.DetailView):     # для вывода актёров
    model = Actor


class Directorslist(generic.ListView):      # для вывода режиссёров
    model = Director
    paginate_by = 5


class Directordetails(generic.DetailView):      # для вывода режиссёров
    model = Director


def buy(request, type):     # для покупки подписки
    user_id = request.user.id       # находим айди юзера, как число
    user_db = User.objects.get(id=user_id)     # находим айди юзера в таблице
    user_sub_type = user_db.groups.all()[0].id     # подписка юзера
    user_group = Group.objects.get(id=user_sub_type)       # группа юзера
    user_group.user_set.remove(user_db)     # удаляем юзера из группы
    group_to_add = Group.objects.get(id=type)       # ищем новую группу (из ссылки, куда надо купить подписку)
    group_to_add.user_set.add(user_db)      # записываем юзера в группу
    sub_type = group_to_add.name
    data = {'subscription': sub_type}
    return render(request, 'buy.html', data)



def registration(request):          # для регистрации
    if request.POST:
        regform = forms.Registration(request.POST)
        if regform.is_valid():
            print('ok')
            regform.save()      # сохраняем данные?
            logininfo = regform.cleaned_data.get('username')
            password = regform.cleaned_data.get('password1')
            user = authenticate(username=logininfo, password=password)
            login(request, user)
            bronze_tier = Group.objects.get(id=1)       # ищем базовую подписку
            bronze_tier.user_set.add(user)              # добавляем её новому пользователю



            # man = User.objects.get(username=logininfo)
            # man.first_name = k1

            return redirect('home')
    else:
        regform = forms.Registration
    data = {'regform': regform}
    return render(request, 'registration/registration.html', data)


def submanager(request):
    user_id = request.user.id       # находим айди юзера, как число
    user_db = User.objects.get(id=user_id)     # находим айди юзера в таблице
    user_sub_type = user_db.groups.all()[0].id     # подписка юзера
    subtier = Group.objects.get(id=user_sub_type)       # группа юзера
    data = {'subtier': subtier, 'user_sub_type': user_sub_type}
    return render(request, 'submanager.html', data)


def switch_to_bronze(request):
    if request.method == 'POST':
        user_id = request.user.id  # находим айди юзера, как число
        user_db = User.objects.get(id=user_id)  # находим айди юзера в таблице
        user_sub_type = user_db.groups.all()[0].id  # подписка юзера
        user_group = Group.objects.get(id=user_sub_type)  # группа юзера
        user_group.user_set.remove(user_db)  # удаляем юзера из группы
        group_to_add = Group.objects.get(id=1)  # ищем новую группу (из ссылки, куда надо купить подписку)
        group_to_add.user_set.add(user_db)  # записываем юзера в группу
        sub_type = group_to_add.name        # выводим имя подписки
        data = {'subscription': sub_type, 'user_sub_type': user_sub_type}
        # return render(request, 'submanager.html', data)
        return render(request, 'buy.html', data)


def switch_to_silver(request):
    if request.method == 'POST':
        user_id = request.user.id  # находим айди юзера, как число
        user_db = User.objects.get(id=user_id)  # находим айди юзера в таблице
        user_sub_type = user_db.groups.all()[0].id  # подписка юзера
        user_group = Group.objects.get(id=user_sub_type)  # группа юзера
        user_group.user_set.remove(user_db)  # удаляем юзера из группы
        group_to_add = Group.objects.get(id=2)  # ищем новую группу (из ссылки, куда надо купить подписку)
        group_to_add.user_set.add(user_db)  # записываем юзера в группу
        sub_type = group_to_add.name        # выводим имя подписки
        data = {'subscription': sub_type, 'user_sub_type': user_sub_type}
        # return render(request, 'submanager.html', data)
        return render(request, 'buy.html', data)


def switch_to_gold(request):
    if request.method == 'POST':
        user_id = request.user.id  # находим айди юзера, как число
        user_db = User.objects.get(id=user_id)  # находим айди юзера в таблице
        user_sub_type = user_db.groups.all()[0].id  # подписка юзера
        user_group = Group.objects.get(id=user_sub_type)  # группа юзера
        user_group.user_set.remove(user_db)  # удаляем юзера из группы
        group_to_add = Group.objects.get(id=3)  # ищем новую группу (из ссылки, куда надо купить подписку)
        group_to_add.user_set.add(user_db)  # записываем юзера в группу
        sub_type = group_to_add.name        # выводим имя подписки
        data = {'subscription': sub_type, 'user_sub_type': user_sub_type}
        # return render(request, 'submanager.html', data)
        return render(request, 'buy.html', data)