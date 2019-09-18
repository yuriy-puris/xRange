from djongo import models

# Create your models here.
class Category(models.Model):
    class Meta:
        abstract = True

    category_id = models.AutoField(primary_key=True)
    category_value = models.TextField()
    parent_id = models.IntegerField()
    category_url = models.TextField()
    category_shop_id = models.IntegerField()

class CategoryMoyo(Category):
    class Meta:
        db_table = "category_moyo"

class CategoryAllo(Category):
    class Meta:
        db_table = "category_allo"

class CategoryEldorado(Category):
    class Meta:
        db_table = "category_eldorado"