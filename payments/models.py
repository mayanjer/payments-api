import random
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True) 
    def save(self, *args, **kwargs):
        if not self.user_name:
            self.user_name = f"{self.first_name[0]}-{self.last_name}".lower()
        return super().save(*args, **kwargs)
    
class Payee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(null =True, blank =True)
    def save(self, *args, **kwargs):
        if not self.user_name:
            self.user_name = f"{self.first_name[0]}-{self.last_name}".lower()
        return super().save(*args, **kwargs)
               
class Payment(models.Model):
    status_choices = [("PENDING", "pending"), ("SUCCESS", "success"), ("FAILED", "failed")]
    payment_method_choices = [("MOBILE_MONEY", "mobile_money"), ("AIRTEL_MONEY", "airtel_money"), ("CASH", "cash")]
    payer = models.ForeignKey('Payer', on_delete=models.SET_NULL, null = True)
    payee = models.ForeignKey('Payee', on_delete=models.SET_NULL, null=True)
    payment_status = models.CharField(max_length=255, choices=status_choices)
    payment_time = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=255)
