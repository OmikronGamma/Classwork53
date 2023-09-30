from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)
# admin.site.register(Director)
# admin.site.register(Actor)
# admin.site.register(Subscription)
admin.site.register(AgeRestriction)
admin.site.register(Country)
# admin.site.register(Movie)


class Actoradmin(admin.ModelAdmin):
    list_display = ('actor_first_name', 'actor_last_name', 'actor_birth_date')      # столбцы в админке
    list_display_links = ('actor_first_name', 'actor_last_name')                    # ссылки для доп столбцов


class Directoradmin(admin.ModelAdmin):
    list_display = ('director_first_name', 'director_last_name')
    list_display_links = ('director_first_name', 'director_last_name')


class Movieadmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    # list_display_links = ('title', 'year', 'director', 'display_actors')
    list_filter = ('subscription', 'genre', 'rating')       # появляется меню с фильтрами в админке
    fieldsets = (('About', {'fields': ('title', 'summary', 'genre')}),     # форматирование/разметка страницы конкретного фильма
                 ('Personalities', {'fields': ('director', 'actors')}),
                 ('Rest', {'fields': ('rating', 'country', 'year', 'age_rate', 'subscription')}))


class Statusinline(admin.TabularInline):
    model = Movie


class Statusadmin(admin.ModelAdmin):
    inlines = [Statusinline]


admin.site.register(Actor, Actoradmin)      # регистрация модели в админку, с указанными  параметрами
admin.site.register(Director, Directoradmin)
admin.site.register(Movie, Movieadmin)
admin.site.register(Subscription, Statusadmin)