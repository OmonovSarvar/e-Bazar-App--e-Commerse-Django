from django.db import models
from django.utils.timezone import now


# Create your models here.
class ProductModel(models.Model):
    product_img = models.ImageField(upload_to='photos/')
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.CharField()
    post_date = models.DateField(default=now)
    location = models.CharField(max_length=80)

    class Meta:
        # ordering = ['-post_date']
        db_table = 'products'


    def __str__(self):
        return f'{self.product_name}'
