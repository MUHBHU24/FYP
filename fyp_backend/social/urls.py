from django.urls import path
from . import api
from . import views


urlpatterns = [
    path('', api.all_messages, name='all_messages'),
    path('new/', api.create_message, name='create_message'),
]