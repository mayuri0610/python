# Generated by Django 4.1.7 on 2023-07-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioadmin', '0019_remove_bannerpage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='github',
            field=models.TextField(blank=True, null=True),
        ),
    ]