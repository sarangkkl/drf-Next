from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_Address(self):
    return Address.objects.filter(user=self)

User.add_to_class("get_Address", get_Address)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    postalCode = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    shippingAddress = models.BooleanField(default=False)
    def __str__(self):
        return self.address