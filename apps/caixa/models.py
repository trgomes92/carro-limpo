from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Caixa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.DateField(default=date.today, unique=True)
    aberto = models.BooleanField(default=True)

class Transacao(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
    type = models.CharField(max_length=3)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=100, blank=True)