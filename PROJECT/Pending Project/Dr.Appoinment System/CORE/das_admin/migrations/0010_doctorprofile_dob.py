# Generated by Django 4.2 on 2023-06-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('das_admin', '0009_remove_doctorprofile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]