# Generated by Django 4.0.1 on 2022-01-28 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=240, verbose_name='Name')),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
