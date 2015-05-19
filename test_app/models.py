from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    relation = models.ForeignKey('self', null=True, blank=True)
