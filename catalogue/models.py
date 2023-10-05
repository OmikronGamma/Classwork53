from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    genre_name = models.CharField(max_length=100, verbose_name='Genre:')

    def __str__(self):
        return self.genre_name


class Director(models.Model):
    director_first_name = models.CharField(max_length=100, verbose_name='Director first name:')
    director_last_name = models.CharField(max_length=100, verbose_name='Director last name:')

    def __str__(self):
        return f'{self.director_last_name}, {self.director_first_name}'

    def get_absolute_url(self):
        return reverse('directorinfo', args=[self.id, self.director_last_name])


class Actor(models.Model):
    actor_first_name = models.CharField(max_length=100, verbose_name='Actor first name:')
    actor_last_name = models.CharField(max_length=100, verbose_name='Actor last name:')
    actor_birth_date = models.DateField(null=True, blank=True, verbose_name='Date of birth:')
    actor_country = models.CharField(max_length=100, verbose_name='Born in _ country:')

    def __str__(self):
        return self.actor_last_name

    def get_absolute_url(self):
        return reverse('actorinfo', args=[self.id, self.actor_last_name])


class Subscription(models.Model):
    subs_selection = (('bronze', 'BRONZE'), ('silver', 'SILVER'), ('gold', 'GOLD'))
    subscription_type = models.CharField(max_length=100, choices=subs_selection, verbose_name='Subscription type:')

    def __str__(self):
        return self.subscription_type



class AgeRestriction(models.Model):
    choice = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    age_restr = models.CharField(max_length=20, choices=choice, verbose_name='Age restriction:')

    def __str__(self):
        return self.age_restr


class Country(models.Model):

    movie_country = models.CharField(max_length=100, verbose_name='Production country:')

    def __str__(self):
        return self.movie_country


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Movie title:')
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_DEFAULT, default=1)
    rating = models.FloatField(verbose_name='Critics score:')
    country = models.ForeignKey(to=Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(to=Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=9999, verbose_name='Movie synopsis:')
    year = models.IntegerField(verbose_name='Production year(s):')
    age_rate = models.ForeignKey(to=AgeRestriction, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(to=Actor, verbose_name='Actors list:')
    subscription = models.ForeignKey(to=Subscription, on_delete=models.SET_NULL, null=True)
    movie_poster = models.CharField(max_length=255, blank=True, null=True, verbose_name='Movie poster:')

    def __str__(self):
        return self.title

    def display_actors(self):
        tempstr = ''
        for a in self.actors.all():
            tempstr += a.actor_last_name + ' '
        return tempstr
    display_actors.short_description = 'Actor(s)'       # замена названия столбца на сайте

    def get_absolute_url(self):
        return reverse('movieinfo', args=[self.id, self.title])


