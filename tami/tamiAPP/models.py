from django.db import models
from vote.models import VoteModel

# Create your models here.
class userSub(VoteModel, models.Model):
    description = models.TextField(blank=False, null=False)
    where       = models.CharField(max_length=100, blank=True, default="anon")
    created_at = models.DateTimeField(auto_now_add=True)
