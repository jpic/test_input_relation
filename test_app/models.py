from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    relation = models.ForeignKey('self', null=True, blank=True)
    name0 = models.CharField(max_length=200, null=True, blank=True)
    name1 = models.CharField(max_length=200, null=True, blank=True)
    name2 = models.CharField(max_length=200, null=True, blank=True)
    name3 = models.CharField(max_length=200, null=True, blank=True,
            choices=[('a', 'a')])
