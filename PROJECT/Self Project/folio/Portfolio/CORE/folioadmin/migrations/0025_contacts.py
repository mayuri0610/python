# Generated by Django 4.1.7 on 2023-07-23 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('folioadmin', '0024_interests_user_projects_user_services_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, default=True, max_length=600, null=True)),
                ('massage', models.TextField(blank=True, default=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
