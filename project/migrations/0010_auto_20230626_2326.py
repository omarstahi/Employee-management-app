# Generated by Django 2.2.12 on 2023-06-26 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_employee_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30, null=True)),
                ('duration', models.DecimalField(decimal_places=0, max_digits=6, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='absence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Absence'),
        ),
    ]
