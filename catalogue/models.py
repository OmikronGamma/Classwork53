from django.db import models

# Create your models here.


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Director(models.Model):
    director_first_name = models.CharField(max_length=100)
    director_last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.director_last_name, self.director_first_name


class Actor(models.Model):
    actor_first_name = models.CharField(max_length=100)
    actor_last_name = models.CharField(max_length=100)
    actor_birth_date = models.DateField(null=True, blank=True)
    actor_country = models.CharField(max_length=100)

    def __str__(self):
        return self.actor_last_name


class Subscription(models.Model):
    subs_selection = (('bronze', 'BRONZE'), ('silver', 'SILVER'), ('gold', 'GOLD'))
    subscription_type = models.CharField(max_length=100, choices=subs_selection)

    def __str__(self):
        return self.subscription_type



class AgeRestriction(models.Model):
    choice = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    age_restr = models.CharField(max_length=20, choices=choice)

    def __str__(self):
        return self.age_restr


class Counrty(models.Model):

    movie_country = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_country


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_DEFAULT, default=1)
    rating = models.FloatField()
    country = models.ForeignKey(to=Counrty, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(to=Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=9999)
    year = models.IntegerField()
    age_rate = models.ForeignKey(to=AgeRestriction, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(to=Actor)
    subscription = models.ForeignKey(to=Subscription, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
