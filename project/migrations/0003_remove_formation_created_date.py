# Generated by Django 2.2.12 on 2023-05-25 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_formation_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='created_date',
        ),
    ]
