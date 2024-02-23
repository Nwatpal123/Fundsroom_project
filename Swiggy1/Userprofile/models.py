from django.db import models

class User(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField(default='example@example.com')
    password = models.TextField(max_length=100, default='default_password')
    address = models.TextField(default='default_address')
    userid = models.IntegerField(primary_key=True)  # Use IntegerField for manual control

    def __str__(self):
        return self.name
