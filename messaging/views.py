'''
Created on 2 Aug 2021

@author: eytan
'''
import json
# import urllib3

from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from messaging.models import Message
from messaging.serializers import MessageSerializer
from messaging.settings import MESSAGE_CLUSTER


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "receipient"
    
    @action(methods=['get'], detail=True)
    def receive(self, request, receipient):
        messages = [ { 'sender': m.sender, 'receipient': m.receipient, 'message': m.body } for m in self.queryset.filter(receipient=receipient)]        
        return Response(messages)
    
    def create(self, request, *args, **kwargs):
#         self._send_to_cluster(request.data)
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)
    
#     def _send_to_cluster(self, data):
#         http = urllib3.HTTPSConnectionPool()
#         url = "http://host:{}/{}"
#         encoded_data = json.dumps(data).encode('utf-8')
#         for host in MESSAGE_CLUSTER:
#             http.request(
#                  'POST',
#                  url.format(host['ip'], host['port']),
#                  body=encoded_data,
#                  headers={'Content-Type': 'application/json'})
