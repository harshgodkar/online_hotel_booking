from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_passwrd = models.CharField(max_length=10)

    def __str__(self):
        return self.username

