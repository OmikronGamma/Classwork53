from django.db import models
from django.urls import reverse

# Create your models here.


class PetIllnessStage(models.Model):
    choice = (('Лёгкая', 'Лёгкая'), ('Средняя', 'Средняя'), ('Тяжёлая', 'Тяжёлая'))
    illness_stage = models.CharField(max_length=100, choices=choice, verbose_name='Форма болезни:')

    def __str__(self):
        return self.illness_stage


class PetIllnessName(models.Model):
    illness_name = models.CharField(max_length=100, verbose_name='Название болезни:')

    def __str__(self):
        return self.illness_name


class Treatment(models.Model):
    drug_title = models.CharField(max_length=100, verbose_name='Название лекарства:')
    drug_dose = models.CharField(max_length=100, verbose_name='Дозировка:')        # ?
    drug_intake = models.IntegerField(verbose_name='Принимать Х раз в день:')
    drug_period = models.IntegerField(verbose_name='Принимать Х дней:')

    def __str__(self):
        return f'{self.drug_title}, {self.drug_dose}, {self.drug_intake} раза в день, в течении {self.drug_period} дней'



class Doctors(models.Model):
    doc_first_name = models.CharField(max_length=100, verbose_name='Имя ветеринара:')
    doc_last_name = models.CharField(max_length=100, verbose_name='Фамилия ветеринара:')

    def __str__(self):
        return f'{self.doc_last_name}, {self.doc_first_name}'


class VetClinic(models.Model):
    pet_name = models.CharField(max_length=100, verbose_name='Кличка:')
    pet_breed = models.CharField(max_length=100, verbose_name='Порода:')
    pet_age = models.IntegerField(verbose_name='Возраст:')
    pet_illness_name = models.ForeignKey(to=PetIllnessName, on_delete=models.SET_NULL, null=True, verbose_name='Название болезни:')
    pet_illness_stage = models.ForeignKey(to=PetIllnessStage, on_delete=models.SET_NULL, null=True, verbose_name='Форма болезни:')
    pet_treatment = models.ManyToManyField(to=Treatment, verbose_name='Название лекарства:')
    assigned_doctor = models.ForeignKey(to=Doctors, on_delete=models.SET_NULL, null=True, verbose_name='Лечащий врач:')

    def __str__(self):
        return self.pet_name

    def get_absolute_url(self):
        return reverse('vetinfo', args=[self.id])
