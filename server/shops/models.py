from djongo import models

# Create your models here.
class ShopTags(models.Model):
  shop_class = models.CharField(max_length=100)

  def __str__(self):
    return self.shop_class

  class Meta:
    abstract = True

class Headers(models.Model):
  shop_headers = models.TextField()

  def __str__(self):
    return self.shop_headers

  class Meta:
    abstract = True

class Shops(models.Model):
  shop_id = models.AutoField(primary_key=True)
  shop_url = models.TextField()