from django.db import models
from Userprofile.models import User
from Restaurant.models import Restaurant

class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurantid = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    delivery_address = models.TextField(default='')
    delivery_groupid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Order ID: {self.orderid}, User ID: {self.userid_id}, Restaurant ID: {self.restaurantid_id}"

    def save(self, *args, **kwargs):
        if not self.pk:
            # If the order is being created for the first time
            existing_orders = Order.objects.filter(restaurantid=self.restaurantid)
            if existing_orders.exists():
                # Get the maximum delivery_groupid
                max_groupid = existing_orders.aggregate(models.Max('delivery_groupid'))['delivery_groupid__max']
                self.delivery_groupid = max_groupid + 1 if max_groupid is not None else 1
            else:
                # If no existing orders from the same restaurant, set delivery_groupid to None
                self.delivery_groupid = None
        
        super(Order, self).save(*args, **kwargs)
