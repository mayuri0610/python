# Generated by Django 4.2.2 on 2023-06-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioadmin', '0004_remove_aboutpage_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
