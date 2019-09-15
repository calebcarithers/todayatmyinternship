from django.db import models

# Create your models here.
class userSub(models.Model):
    description = models.TextField(blank=True, null=True)
    where       = models.CharField(max_length=100, null=False, blank=False)
