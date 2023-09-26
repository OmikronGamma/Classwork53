from django.db import models

# Create your models here.


class PetIllness(models.Model):
    choice = (('Light', 'Light'), ('Mild', 'Mild'), ('Severe', 'Severe'))
    illness_name = models.CharField(max_length=100)
    illness_stage = models.CharField(max_length=100, choices=choice)

    def __str__(self):
        return self.illness_name


class Treatment(models.Model):
    drug_title = models.CharField(max_length=100)
    drug_dose = models.CharField(max_length=100)        # ?
    drug_intake = models.CharField(max_length=100)
    drug_period = models.IntegerField()

    def __str__(self):
        return self.drug_title



class Doctors(models.Model):
    doc_first_name = models.CharField(max_length=100)
    doc_last_name = models.CharField(max_length=100)


class VetClinic(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100)
    pet_age = models.IntegerField()
    pet_illness = models.ForeignKey(to=PetIllness, on_delete=models.SET_NULL, null=True)
    pet_treatment = models.ManyToManyField(to=Treatment)
    assigned_doctor = models.ForeignKey(to=Doctors, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pet_name

