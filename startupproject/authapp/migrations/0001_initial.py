# Generated by Django 4.2.2 on 2023-06-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
