# Generated by Django 4.2.7 on 2023-12-05 03:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Costumers', '0008_lessormodel_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessormodel',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
