# Generated by Django 2.2.12 on 2023-06-27 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20230627_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='absence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='absences', to='project.Absence'),
        ),
    ]
