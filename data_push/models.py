import enum

from django.db import models

# Create your models here.


from django.db import models


class HttpChoice(models.TextChoices):
    GET = 'GET'
    POST = 'POST'
    PATCH = 'PATCH'
    PUT = 'PUT'
    DELETE = 'DELETE'


class Account(models.Model):
    objects = None
    pid = models.BigAutoField(primary_key=True)
    account_id = models.CharField(max_length=30, unique=True, default=None)
    account_name = models.CharField(max_length=30)
    app_secret = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True, default=None)
    website = models.CharField(max_length=30)

    def __repr__(self):
        return "<Account %s>" % self.pid


class Destination(models.Model):
    objects = None
    acc_key = models.ForeignKey(Account, on_delete=models.CASCADE)
    pid = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=100)
    http_method = models.CharField(choices=HttpChoice.choices, max_length=10)
    headers = models.JSONField()

    def __repr__(self):
        return "<Destination %s>" % self.pid
