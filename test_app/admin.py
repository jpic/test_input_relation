from django.contrib import admin

from .models import TestModel


class TestAdmin(admin.ModelAdmin):
    fields = (('name', 'relation'),('name0', 'name1'),('name2', 'name3'))
admin.site.register(TestModel, TestAdmin)
