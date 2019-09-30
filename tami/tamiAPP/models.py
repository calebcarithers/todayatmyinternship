from django.db import models

# Create your models here.
class userSub(models.Model):
    description = models.TextField(blank=False, null=False)
    where       = models.CharField(max_length=100, blank=True, default="anon")
    rank        = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)