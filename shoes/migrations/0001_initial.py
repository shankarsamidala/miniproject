# Generated by Django 4.2.7 on 2023-11-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('rating', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=250)),
            ],
        ),
    ]
