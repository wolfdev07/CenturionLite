from django.db import models
from django.contrib.auth.models import User
from Brokers.models import Broker
from CenturionApi.models import Settlement
from Costumers.utils import save_id_document, save_deeds, save_proof_address, save_acount_lessor
# Create your models here.


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


class LessorAddressModel(models.Model):
    lessor = models.ForeignKey(LessorModel, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=60)
    internal_number = models.CharField(max_length=20, null=True, blank=True)
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lessor.user.username} {self.lessor.user.last_name} - address"



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

    neighbor = models.ForeignKey(Settlement, on_delete=models.CASCADE)
    street = models.CharField(max_length=120)
    number = models.CharField(max_length=60)
    internal_number = models.CharField(max_length=60, null=True, blank=True)
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

Aqui inician los modelos de Arrendatario

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
    finish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.broker.agency.name}"
    

class TenantSocioEconomicModel(models.Model):

    income_per_month =  models.CharField(max_length=400, blank=True, null=True)
    
    civil_status = models.CharField(max_length=120, blank=True, null=True)
    last_grade_of_school = models.CharField(max_length=120, blank=True, null=True)
    pets = models.CharField(max_length=120, blank=True, null=True)