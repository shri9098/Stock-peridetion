from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Currencies(models.Model):
    currencies = models.CharField(max_length=12 ,unique=True)
    def __str__(self):
        return self.currencies



class TradingData(models.Model):
    currency  = models.ForeignKey(Currencies,on_delete=models.CASCADE)
    price = models.FloatField()
    open_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    change_percentage = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.currency.currencies

class UserHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    currency = models.CharField(max_length=20,null=True)
    price = models.FloatField()
    action = models.CharField(max_length=10)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class NotifyData(models.Model):
    msg = models.CharField(max_length=500)
    send_to_all = models.BooleanField(default=False)


class PredictionData(models.Model):
    pair = models.CharField(max_length=10)
    bid = models.FloatField()
    ask = models.FloatField()
    opn = models.FloatField(default=0)
    high = models.FloatField()
    low = models.FloatField()
    chg_percent = models.FloatField()
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.pair