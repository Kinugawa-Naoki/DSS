from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.
class DeliverableInfo(models.Model):
    user_id = models.CharField(max_length=100)
    deliverable_name = models.CharField(max_length=100)
    git_url = models.URLField()
    category = models.CharField(max_length=100)
    languages = models.CharField(max_length=50)
    own_comment = models.CharField(max_length=100, null=True, blank=True)
    created_dt = models.DateTimeField(default=timezone.now)
    modified_dt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.deliverable_name