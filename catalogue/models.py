from django.db import models

# Create your models here.


# class PetName(models.Model):
#     pet_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.pet_name


# class PetBreed(models.Model):
#     pet_breed = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.pet_breed


# class PetAge(models.Model):
#     pet_age = models.IntegerField()
#
#     def __str__(self):
#         return self.pet_age


class PetIllness(models.Model):
    illness_name = models.CharField(max_length=100)
    illness_stage = models.IntegerField()

    def __str__(self):
        return self.illness_name


class Treatment(models.Model):
    drug_title = models.CharField(max_length=100)
    drug_dose = models.CharField(max_length=100)        # ?
    drug_intake = models.CharField(max_length=100)
    drug_period = models.IntegerField()

    def __str__(self):
        return self.drug_title


class VetClinic(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_breed = models.CharField(max_length=100)
    pet_age = models.IntegerField()
    pet_illness = models.ForeignKey(to_fields=PetIllness, on_delete=models.SET_NULL, null=True)
    pet_treatment = models.ManyToManyField(to=Treatment)

    def __str__(self):
        return self.pet_name

