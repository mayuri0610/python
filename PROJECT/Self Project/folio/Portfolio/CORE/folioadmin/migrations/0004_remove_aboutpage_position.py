# Generated by Django 4.2.2 on 2023-06-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folioadmin', '0003_alter_aboutpage_profilepic1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='position',
        ),
    ]
