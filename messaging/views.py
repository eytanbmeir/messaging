'''
Created on 2 Aug 2021

@author: eytan
'''
from messaging.models import Message
from messaging.serializers import MessageSerializer
from rest_framework import viewsets
from django.http.response import Http404
from rest_framework.decorators import action
from rest_framework.response import Response



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "receipient"
    
    @action(methods=['get'], detail=True)
    def receive(self, request, receipient):
        messages = [ { 'sender': m.sender, 'receipient': m.receipient, 'message': m.body } for m in self.queryset.filter(receipient=receipient)]
        return Response(messages)
    
    
        
