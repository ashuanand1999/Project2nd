from django.db import models

class CustomerData(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    customer_mobile = models.BigIntegerField()
    customer_email = models.EmailField(max_length=100)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_cost = models.IntegerField()
    Number_of_products = models.IntegerField()

