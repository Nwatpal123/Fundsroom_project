from django.db import models

class Restaurant(models.Model):
    restaurantid = models.IntegerField(primary_key=True)  # Define restaurantid as an IntegerField
    restaurantname = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.restaurantname
