from django.contrib.auth.models import User
from django.db import models

class CustomerMessage(models.Model):
    user_id =models.AutoField(primary_key=True)
    sender_name = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    agent_response = models.TextField(blank=True, null=True)

