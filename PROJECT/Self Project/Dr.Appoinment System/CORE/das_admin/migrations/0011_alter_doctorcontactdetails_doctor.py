# Generated by Django 4.2 on 2023-06-05 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('das_admin', '0010_doctorprofile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorcontactdetails',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='das_admin.doctorprofile'),
        ),
    ]
