# Generated by Django 2.2.12 on 2023-06-30 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20230630_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absence',
            name='emp',
        ),
        migrations.AddField(
            model_name='absence',
            name='emp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='absences', to='project.Employee'),
        ),
    ]
