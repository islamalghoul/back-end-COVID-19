# Generated by Django 4.1.4 on 2022-12-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_covid_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='Country',
            field=models.CharField(max_length=255),
        ),
    ]
