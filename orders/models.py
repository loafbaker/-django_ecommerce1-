from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from carts.models import Cart
from decimal import Decimal

User = get_user_model()


STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)

class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
    # add address
    sub_total = models.DecimalField(default=Decimal(str(10.99)), max_digits=1000, decimal_places=2) # Python 2.6 do not support Decimal
    tax_total = models.DecimalField(default=Decimal(str(0.99)), max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=Decimal(str(10.99)), max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.order_id
