from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    birthdate = models.DateField()

class Place(models.Model):
    place = models.CharField(max_length=100)

class Booking(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
