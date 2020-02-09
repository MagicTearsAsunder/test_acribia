from django.db import models


class Response(models.Model):
    response = models.CharField(max_length=150)


class Url(models.Model):
    url = models.URLField(max_length=200)
