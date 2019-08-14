from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_value = models.TextField()
    parent_id = models.IntegerField()
    category_url = models.TextField()
    category_shop_id = models.IntegerField()