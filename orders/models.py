from django.db import models


# Create your models here.


class Order(models.Model):
    trans_id = models.CharField(blank=True, max_length=9)
    item = models.CharField(blank=True, max_length=9)
