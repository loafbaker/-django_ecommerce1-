from django.db.models.signals import m2m_changed

from .models import Product, Variation

def product_defaults(sender, instance, action, reverse, *args, **kwargs):
    if action == 'post_add' and not reverse:
        categories = instance.category.all()
        for cat in categories:
            if cat.title == 'T-shirt':
                small_size = Variation.objects.get_or_create(product=instance,
                                                             category='size',
                                                             title='Small')
                medium_size = Variation.objects.get_or_create(product=instance,
                                                              category='size',
                                                              title='Medium')
                large_size = Variation.objects.get_or_create(product=instance,
                                                             category='size',
                                                             title='Large')
                

m2m_changed.connect(product_defaults, sender=Product.category.through)

