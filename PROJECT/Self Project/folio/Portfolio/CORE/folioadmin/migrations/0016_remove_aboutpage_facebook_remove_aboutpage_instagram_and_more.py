# Generated by Django 4.1.7 on 2023-07-05 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folioadmin', '0015_delete_socialaccount_remove_aboutpage_birthday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='linkdin',
        ),
    ]