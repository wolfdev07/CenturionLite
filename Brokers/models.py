from django.db import models
from django.contrib.auth.models import User
from Brokers.utils import agency_brand_path
# Create your models here.


class Agencies(models.Model):
    name = models.CharField(max_length=250)
    brand = models.FileField(upload_to=agency_brand_path)
    is_active = models.BooleanField(default=False)
    membership =  models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.membership}"


class Broker(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agencies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.agency.name}"
