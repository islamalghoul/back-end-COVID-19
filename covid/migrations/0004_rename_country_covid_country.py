# Generated by Django 4.1.4 on 2022-12-24 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_alter_covid_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid',
            old_name='Country',
            new_name='country',
        ),
    ]
