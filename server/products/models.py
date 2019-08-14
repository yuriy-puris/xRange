from djongo import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_shop_id = models.IntegerField()
    product_title = models.TextField()
    product_description = models.TextField(blank=True)

class MyShopTags(models.Model):
    tag_key = models.CharField(max_length=100)
    tag_valuee = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.tag_key

class MyShops(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_url = models.TextField()
    shop_card_tags = models.ArrayModelField(
        model_container = MyShopTags,
    )

    
