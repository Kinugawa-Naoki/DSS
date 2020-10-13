from django.db import models
from django.db.models.fields import CharField
from django.urls import timezone

# Create your models here.
class DeliverableInfo(models.Model):
    name = models.CharField(max_length=100)
    git_url = models.URLField()
    category = models.CharField(max_length=100)
    languages = models.CharField(max_length=50)
    option = models.CharField(max_length=100, null=True, blank=True)
    created_dt = models.DateTimeField(default=timezone.now)
    modified_dt = models.DateTimeField(null=True, blank=True)