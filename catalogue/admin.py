from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(PetIllnessStage)
admin.site.register(Doctors)
admin.site.register(Treatment)
admin.site.register(VetClinic)
admin.site.register(PetIllnessName)


