"""messaging URL Configuration

"""

from django.urls import path
from messaging.views import MessageViewSet
from rest_framework.urlpatterns import format_suffix_patterns

message_send_view = MessageViewSet.as_view({'post':'create'})
message_receive_view = MessageViewSet.as_view({'get':'receive'})

urlpatterns = format_suffix_patterns ([
    
    path('messages/send/', message_send_view, name='create-message'),
    path('messages/<str:receipient>/receive/', message_receive_view, name='retrieve-messages'),
])
