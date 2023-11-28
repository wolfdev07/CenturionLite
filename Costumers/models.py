from django.db import models
from django.contrib.auth.models import User
from Brokers.models import Broker
# Create your models here.


class LessorModel(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)
    curp = models.CharField(max_length=120, unique=True)
    elector_key = models.CharField(max_length=120, unique=True)
    rfc = models.CharField(max_length=60, blank=True, null=True)
    birthday = models.DateField()
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



