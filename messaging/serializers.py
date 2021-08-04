'''
Created on 2 Aug 2021

@author: eytan
'''

from rest_framework import serializers
from messaging.models import Message

# Serializers define the API representation.
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'receipient', 'body']
        lookup_field = "receipient"
