# Generated by Django 2.2.12 on 2023-06-30 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_absence_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='absence',
            old_name='employee',
            new_name='emp',
        ),
    ]