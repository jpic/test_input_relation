from django.contrib import admin

from .models import TestModel


class TestAdmin(admin.ModelAdmin):
    fields = (('name', 'relation'),)
admin.site.register(TestModel, TestAdmin)
