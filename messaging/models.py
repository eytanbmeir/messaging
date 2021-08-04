'''
Created on 2 Aug 2021

@author: eytan
'''
from django.db import models
class Message(models.Model):
    
    sender = models.CharField(max_length = 30)
    receipient = models.CharField(max_length = 30)
    body = models.CharField(max_length = 1024)
    
    class Meta:
        app_label = 'messaging'
        db_table = 'messages'
            
