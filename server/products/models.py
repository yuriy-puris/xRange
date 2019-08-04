from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_shop_id = models.IntegerField()
    product_title = models.TextField()
    product_description = models.TextField(blank=True)