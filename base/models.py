from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class credential(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=80, null=False, blank=False)
    password = models.CharField(max_length=90, null=False, blank=False)
    owned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
