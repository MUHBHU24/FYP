from django.urls import path
from . import views, api


urlpatterns = [
    path('', api.all_messages, name='all_messages'),
]