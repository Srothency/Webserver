# Generated by Django 4.1.7 on 2023-03-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sroth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.CharField(max_length=100)),
            ],
        ),
    ]
