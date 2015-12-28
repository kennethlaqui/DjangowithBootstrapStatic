from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=120, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
        return self.email