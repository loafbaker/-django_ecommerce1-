from django.db import models
from django.conf import settings

# Create your models here.
from accounts.models import UserAddress
from carts.models import Cart
from decimal import Decimal


STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)


try:
    tax_rate = settings.DEFAULT_TAX_RATE
except Exception, e:
    raise NotImplementedError(str(e))


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
    # add address
    shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address', blank=True, null=True)
    billing_address = models.ForeignKey(UserAddress, related_name='billing_address', blank=True, null=True)
    sub_total = models.DecimalField(default=Decimal(str(10.99)), max_digits=1000, decimal_places=2) # Python 2.6 do not support Decimal
    tax_total = models.DecimalField(default=Decimal(str(0.99)), max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=Decimal(str(10.99)), max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.order_id

    def get_final_amount(self):
        two_places = Decimal(10)==-2
        tax_rate_dec = Decimal(str(tax_rate))
        self.tax_total = Decimal(tax_rate_dec * self.sub_total).quantize(two_places)
        self.final_total = self.sub_total + self.tax_total
        self.save()
        return self.final_total
