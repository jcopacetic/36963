from django.db import models
from users.models import User

class Company(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  company_name = models.CharField(max_length=254, unique=True)
  Address = models.CharField(max_length=300, unique=False)
  city = models.CharField(max_length=100, unique=False)
  province = models.CharField(max_length=25, unique=False)
  region = models.CharField(max_length=25, unique=False)
  country = models.CharField(max_length=25, unique=False)
  phone = models.CharField(max_length=11, unique=False)
  description = models.CharField(max_length=500, unique=False)
