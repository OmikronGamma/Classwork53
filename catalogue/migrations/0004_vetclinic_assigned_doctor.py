# Generated by Django 4.2.5 on 2023-09-26 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_doctors_alter_petillness_illness_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetclinic',
            name='assigned_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.doctors'),
        ),
    ]
