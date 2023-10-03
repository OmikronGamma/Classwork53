from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    pets_amount = VetClinic.objects.all().count()
    docs_amount = Doctors.objects.all().count()
    light_illness_amount = VetClinic.objects.filter(pet_illness_stage__vetclinic=1).count()
    data = {'pets_amount': pets_amount, 'docs_amount': docs_amount, 'light_illness_amount': light_illness_amount}
    return render(request, 'index.html', data)


class Vetlist(generic.ListView):
    model = VetClinic


class Vetdetails(generic.DetailView):
    model = VetClinic
