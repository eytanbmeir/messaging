'''
Created on 3 Aug 2021

@author: eytan
'''
from django.test import TestCase
from messaging.urls import message_receive_view
from rest_framework.test import APIRequestFactory 
from messaging.models import Message

class TestMessageView(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self._factory = APIRequestFactory()
        self._insert_messages([
            {'sender':'kuku', 'receipient':'kiki', 'body':'Hello There!'},
            {'sender':'kuku', 'receipient':'kiki', 'body':'Hiiiiiiiiiiiiii'},
            {'sender':'kuku', 'receipient':'koko', 'body':'Hello There!'},
            {'sender':'koko', 'receipient':'kiki', 'body':'Hello There!'},
            {'sender':'kuku', 'receipient':'kiki', 'body':'Blaaaaaaaaaa'},
            ])
        
    def _insert_messages(self, messages):
        Message.objects.bulk_create([Message(**m) for m in messages])
    
    def test_receive_4_messages(self):
        request = self._factory.get(path='messages')
        response = message_receive_view(request, 'kiki')
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, len(response.data))
        
    def test_receive_no_messages(self):
    
        request = self._factory.get(path='messages')
        response = message_receive_view(request, 'kaka')
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.data)
        
        
        