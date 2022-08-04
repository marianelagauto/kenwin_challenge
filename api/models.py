from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models import Sum


class Product(models.Model):
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField(default=0)

    def check_stock(self, cuantity):
        if self.stock < cuantity:
            raise ValidationError("El stock no es suficiente",code="invalid")

    def decrease_stock(self, cuantity):
        self.stock = self.stock - cuantity

    def restore_stock(self, cuantity):
        # entiendo que aca no es necesario ver si cuantity > 0
        self.stock = self.stock + cuantity

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    @property
    def get_total(self):
        return OrderDetail.objects.filter(order=self).aggregate(Sum('product__price'))['product__price__sum']

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name="details", on_delete=models.CASCADE)
    cuantity = models.IntegerField(validators=[MinValueValidator(1)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)