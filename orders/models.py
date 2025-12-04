from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.name
    
PAYMENT_METHOD_CHOICES =[ 
    ("YAPE", "Yape"),
    ("PLIN" , "Plin"),
    ("CASH", "cash")
]

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.created_at:%Y-%m-%d %H:%M}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def line_total(self):
        return self.unit_price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
