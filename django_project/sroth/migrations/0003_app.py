# Generated by Django 4.1.7 on 2023-05-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sroth', '0002_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]