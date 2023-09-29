from django.contrib import admin
from .models import *

# Register your models here.


class Docadmin(admin.ModelAdmin):
    list_display = ('doc_first_name', 'doc_last_name')      # столбцы в админке
    list_display_links = ('doc_first_name', 'doc_last_name')                    # ссылки для доп столбцов


class VetClinicadmin(admin.ModelAdmin):
    # list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('pet_name', 'assigned_doctor', 'pet_illness_name')       # появляется меню с фильтрами в админке
    fieldsets = (('Сведения о животинке', {'fields': ('pet_name', 'pet_age', 'pet_breed')}),     # форматирование/разметка страницы конкретного фильма
                 ('Лечение', {'fields': ('assigned_doctor', 'pet_illness_name', 'pet_illness_stage', 'pet_treatment')}),
                 )





admin.site.register(PetIllnessStage)
admin.site.register(Doctors, Docadmin)
admin.site.register(Treatment)
admin.site.register(VetClinic, VetClinicadmin)
admin.site.register(PetIllnessName)


