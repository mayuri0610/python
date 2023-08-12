# Generated by Django 4.2 on 2023-05-24 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
                ('state_pic', models.ImageField(blank=True, null=True, upload_to='State pic')),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.country_model')),
            ],
        ),
    ]
