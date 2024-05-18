from django.db import models

# Create your models here.
class Users(models.Model):
    lastname = models.CharField('lstname', max_length=50)
    firstname = models.CharField('firstname', max_length=50)
    patronymic = models.CharField('patronymic', max_length=50)
    login = models.CharField('login', max_length=100)
    password = models.CharField('password', max_length=100)
    mail = models.CharField('password', max_length=100)

    def __str__(self):
        return self.login
