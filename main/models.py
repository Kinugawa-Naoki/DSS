from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.
class DeliverableInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    deliverable_name = models.CharField(max_length=100)
    git_url = models.URLField()
    category = models.CharField(max_length=100)
    languages = models.CharField(max_length=50)
    own_comment = models.CharField(max_length=100, null=True, blank=True)
    non_display = models.CharField(max_length=6, null=True, blank=True)
    created_dt = models.DateTimeField(default=timezone.now)
    modified_dt = models.DateTimeField(null=True, blank=True)
    good = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.deliverable_name

class PablicComment(models.Model):
    deliverable_id = ForeignKey(DeliverableInfo, to_field='id', on_delete=models.CASCADE)
    post_user_id = models.CharField(max_length=100)
    comment = models.TextField(max_length=140)