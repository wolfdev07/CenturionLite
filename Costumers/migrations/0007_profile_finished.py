# Generated by Django 4.2.7 on 2023-12-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Costumers', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
