import enum

from django.db import models

# Create your models here.


from django.db import models


class HttpChoice(enum.Enum):
    GET = 1
    POST = 2
    PATCH = 3
    PUT = 4
    DELETE = 5


class Account(models.Model):
    objects = None
    pid = models.BigAutoField(primary_key=True)
    account_id = models.CharField(max_length=30)
    account_name = models.CharField(max_length=30)
    app_secret = models.CharField(max_length=30)
    website = models.CharField(max_length=30)

    def __repr__(self):
        return "<Account %s>" % self.pid


class Destination(models.Model):
    objects = None
    acc_key = models.ForeignKey(Account, on_delete=models.CASCADE)
    pid = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=30)
    http_method = models.CharField(max_length=10, choices=[(choice, choice.value) for choice in HttpChoice])
    headers = models.JSONField()

    def __repr__(self):
        return "<Destination %s>" % self.pid
