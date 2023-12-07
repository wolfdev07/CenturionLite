# Generated by Django 4.2.7 on 2023-12-07 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Costumers', '0012_leasepropertymodel_cfe_service_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leasepropertymodel',
            name='avaible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='leasepropertymodel',
            name='property_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Costumers.addressmodel'),
        ),
    ]
