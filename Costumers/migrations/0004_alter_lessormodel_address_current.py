# Generated by Django 4.2.7 on 2023-11-29 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Costumers', '0003_leasepropertymodel_lessor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessormodel',
            name='address_current',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Costumers.addressmodel'),
        ),
    ]
