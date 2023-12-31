# Generated by Django 4.1.7 on 2023-07-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('das_admin', '0012_alter_doctorprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorqualification',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctorservice',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctorspeciality',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='completion_year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='degree',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='seat_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='service',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='speciality',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='starting_year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='university',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DoctorContactDetails',
        ),
        migrations.DeleteModel(
            name='DoctorQualification',
        ),
        migrations.DeleteModel(
            name='DoctorService',
        ),
        migrations.DeleteModel(
            name='DoctorSpeciality',
        ),
    ]
