from django.db import models
from django.contrib.auth.models import User
from Brokers.models import Broker
from CenturionApi.models import Settlement
from Costumers.utils import *
# Create your models here.


"""
ESTE MODELO SE OCUPARA PARA PODER SER USADO PARA DIRECCIONES

"""

class AddressModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=60)
    internal_number = models.CharField(max_length=20, null=True, blank=True)
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - address"


class ReferencesModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    relationship = models.CharField(max_length=120)
    relationship_time = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.user} Referencia"



class LessorModel(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)
    curp = models.CharField(max_length=120, unique=True, blank=True, null=True)
    elector_key = models.CharField(max_length=120, unique=True, blank=True, null=True)
    rfc = models.CharField(max_length=60, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender =  models.CharField(max_length=120, blank=True, null=True)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    membership = models.CharField(max_length=20)
    address_current = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.broker.agency.name} "


class DataPaymentModel(models.Model):

    lessor = models.ForeignKey(LessorModel, on_delete=models.CASCADE)
    bank = models.CharField(max_length=120)
    interbank_account = models.CharField(max_length=200)
    account = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.bank} - {self.account}'


class LessorDocumentsModel(models.Model):

    lessor = models.ForeignKey(LessorModel, on_delete=models.CASCADE)
    document_identification_front = models.FileField(upload_to=save_id_document)
    document_identification_back = models.FileField(upload_to=save_id_document) 
    document_deed_property = models.FileField(upload_to=save_deeds)
    proof_address = models.FileField(upload_to=save_proof_address)
    acount_bank = models.FileField(upload_to=save_acount_lessor)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lessor.user.username} {self.lessor.user.last_name} - documents"


class LeasePropertyModel(models.Model):

    lessor = models.ForeignKey(LessorModel, on_delete=models.CASCADE, blank=True, null=True)
    property_address =  models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    location = models.CharField(max_length=500, null=True, blank=True)
    avaible = models.BooleanField(default=False)
    rental_price = models.CharField(max_length=350)
    maintenance_price = models.CharField(max_length=350)
    maintenance_included = models.BooleanField()
    finish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street} {self.number} {self.neighbor.postal_code.city.name} {self.neighbor.postal_code.city.state.name}"
    



""" 

MODELOS DE ARRENDATARIO

"""


class TenantModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)
    curp = models.CharField(max_length=120, unique=True, blank=True, null=True)
    elector_key = models.CharField(max_length=120, unique=True, blank=True, null=True)
    rfc = models.CharField(max_length=60, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender =  models.CharField(max_length=120, blank=True, null=True)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    membership = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    house_in_perspective = models.ForeignKey(LeasePropertyModel, on_delete=models.CASCADE)
    is_owner =  models.BooleanField(default=True)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.broker.agency.name}"
    

class TenantEconomicModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_per_month =  models.CharField(max_length=400)
    name_labor_source = models.CharField(max_length=120)
    company_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    phone_company = models.CharField(max_length=120)
    ocupation = models.CharField(max_length=120)
    other_incomes = models.TextField(max_length=600)

    def __str__(self):
        return f"{self.user} Analisis Economico"



class TenantSocioModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    previous_address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    civil_status = models.CharField(max_length=120)
    economic_dependents = models.CharField(max_length=120)
    spouse_name = models.CharField(max_length=120, blank=True, null=True)
    spouse_income = models.CharField(max_length=120, blank=True, null=True)
    last_grade_of_school = models.CharField(max_length=120)
    pets = models.CharField(max_length=120)
    pet_breed = models.CharField(max_length=120)
    cohabitants = models.CharField(max_length=120)
    car_brand = models.CharField(max_length=120)
    car_plates = models.CharField(max_length=120)
    reason_to_rent = models.TextField(max_length=120)

    def __str__(self):
        return f"{self.user} Entorno Social"


class SolidarityEconomicModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_address = models.ForeignKey(AddressModel, related_name='company_solidarity_models', on_delete=models.CASCADE)
    income_per_month =  models.CharField(max_length=400)
    name_labor_source = models.CharField(max_length=120)
    company_address = models.ForeignKey(AddressModel, related_name='current_solidarity_models', on_delete=models.CASCADE)
    phone_company = models.CharField(max_length=120)
    ocupation = models.CharField(max_length=120)
    other_incomes = models.TextField(max_length=600)

    def __str__(self):
        return f"{self.user} Analisis Economico"



class TenantDocumentsModel(models.Model):
    
    tenant = models.ForeignKey(TenantModel, on_delete=models.CASCADE)
    document_identification_front = models.FileField(upload_to=save_id_document)
    document_identification_back = models.FileField(upload_to=save_id_document)
    proof_address = models.FileField(upload_to=save_proof_address)
    first_receipt = models.FileField(upload_to=save_acount_tenant)
    second_receipt = models.FileField(upload_to=save_acount_tenant)
    third_receipt = models.FileField(upload_to=save_acount_tenant)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.lessor.user.username} {self.lessor.user.last_name} - documents"