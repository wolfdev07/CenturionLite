# Generated by Django 4.2.7 on 2023-12-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Costumers', '0007_profile_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessormodel',
            name='nationality',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
