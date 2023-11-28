# Generated by Django 4.2.7 on 2023-11-28 11:08

import Costumers.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CenturionApi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Brokers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=60)),
                ('internal_number', models.CharField(blank=True, max_length=20, null=True)),
                ('settlement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CenturionApi.settlement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeasePropertyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('avaible', models.BooleanField(default=False)),
                ('rental_price', models.CharField(max_length=350)),
                ('maintenance_price', models.CharField(max_length=350)),
                ('maintenance_included', models.BooleanField()),
                ('finish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('property_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.addressmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TenantSocioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civil_status', models.CharField(max_length=120)),
                ('economic_dependents', models.CharField(max_length=120)),
                ('spouse_name', models.CharField(blank=True, max_length=120, null=True)),
                ('spouse_income', models.CharField(blank=True, max_length=120, null=True)),
                ('last_grade_of_school', models.CharField(max_length=120)),
                ('pets', models.CharField(max_length=120)),
                ('pet_breed', models.CharField(max_length=120)),
                ('cohabitants', models.CharField(max_length=120)),
                ('car_brand', models.CharField(max_length=120)),
                ('car_plates', models.CharField(max_length=120)),
                ('reason_to_rent', models.TextField(max_length=120)),
                ('previous_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.addressmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TenantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=250)),
                ('curp', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('elector_key', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('rfc', models.CharField(blank=True, max_length=60, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=120, null=True)),
                ('occupation', models.CharField(blank=True, max_length=250, null=True)),
                ('membership', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_owner', models.BooleanField(default=True)),
                ('finish', models.BooleanField(default=False)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Brokers.broker')),
                ('house_in_perspective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.leasepropertymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TenantEconomicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_per_month', models.CharField(max_length=400)),
                ('name_labor_source', models.CharField(max_length=120)),
                ('phone_company', models.CharField(max_length=120)),
                ('ocupation', models.CharField(max_length=120)),
                ('other_incomes', models.TextField(max_length=600)),
                ('company_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.addressmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolidarityEconomicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_per_month', models.CharField(max_length=400)),
                ('name_labor_source', models.CharField(max_length=120)),
                ('phone_company', models.CharField(max_length=120)),
                ('ocupation', models.CharField(max_length=120)),
                ('other_incomes', models.TextField(max_length=600)),
                ('company_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_solidarity_models', to='Costumers.addressmodel')),
                ('current_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_solidarity_models', to='Costumers.addressmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReferencesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('relationship', models.CharField(max_length=120)),
                ('relationship_time', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=250)),
                ('curp', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('elector_key', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('rfc', models.CharField(blank=True, max_length=60, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=120, null=True)),
                ('occupation', models.CharField(blank=True, max_length=250, null=True)),
                ('membership', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finish', models.BooleanField(default=False)),
                ('address_current', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.addressmodel')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Brokers.broker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessorDocumentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_identification_front', models.FileField(upload_to=Costumers.utils.save_id_document)),
                ('document_identification_back', models.FileField(upload_to=Costumers.utils.save_id_document)),
                ('document_deed_property', models.FileField(upload_to=Costumers.utils.save_deeds)),
                ('proof_address', models.FileField(upload_to=Costumers.utils.save_proof_address)),
                ('acount_bank', models.FileField(upload_to=Costumers.utils.save_acount_lessor)),
                ('finish', models.BooleanField(default=False)),
                ('lessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.lessormodel')),
            ],
        ),
        migrations.CreateModel(
            name='DataPaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=120)),
                ('interbank_account', models.CharField(max_length=200)),
                ('account', models.CharField(blank=True, max_length=200, null=True)),
                ('lessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Costumers.lessormodel')),
            ],
        ),
    ]