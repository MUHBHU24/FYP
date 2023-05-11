from django.urls import path
from . import api
from . import views


urlpatterns = [
    path('', api.all_messages, name='all_messages'),
    path('new/', api.create_message, name='create_message'),
    path('<int:id>/upvote/', api.upvote, name='upvote'),
    path('<int:id>/', api.expandMessage, name='reply'), # <int:id>/reply
    path('<int:id>/sendReply/', api.sendReply, name='sendReply'),
    # path('account/<int:primary_key>/', api.account, name='account'),
]