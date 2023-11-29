from django.db import models


class State(models.Model):
    number = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class PostalCode(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    code = models.CharField(max_length=250)

    def __str__(self):
        return self.code



class Settlement(models.Model):
    postal_code = models.ForeignKey(PostalCode, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    settlement_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MembershipModel(models.Model):
    membership = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.membership