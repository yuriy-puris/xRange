from djongo import models

# Create your models here.
class ShopTags(models.Model):
  class Meta:
    abstract = True

  tag_key = models.CharField(max_length=100)
  tag_value = models.CharField(max_length=100)

  def __str__(self):
    return self.tag_key

class Shops(models.Model):
  shop_id = models.AutoField(primary_key=True)
  shop_url = models.TextField()
  shop_tags = models.ArrayModelField(
    model_container = ShopTags
  )