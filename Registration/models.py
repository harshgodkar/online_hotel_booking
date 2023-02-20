from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_passwrd = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Customer(models.Model):
    cust_id = models.IntegerField()
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email_id = models.EmailField()
    dob = models.DateField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    payment_id = models.IntegerField()
    cus_id = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    payment_amt = models.IntegerField()
    payment_date = models.DateField()

class Booking(models.Model):
    booking_id = models.IntegerField()
    booking_desc = models.TextField()
    booking_date = models.DateField()

class Room(models.Model):
    room_id = models.IntegerField()
    room_no = models.CharField(max_length=10)
    room_type = models.CharField(max_length=30)
    room_desc = models.TextField()

class Receptionist(models.Model):
    res_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()