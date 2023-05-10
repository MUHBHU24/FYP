from django.urls import path
from . import api
from . import views


urlpatterns = [
    path('', api.all_messages, name='all_messages'),
    path('new/', api.create_message, name='create_message'),
    path('<int:primary_key>/upvote/', api.upvote, name='upvote'),
    path('<int:primary_key>/reply/', api.expandMessage, name='reply'),
    # path('account/<int:primary_key>/', api.account, name='account'),
]