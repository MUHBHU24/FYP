from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import MessageSerializer
from .models import Message, Picture
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def all_messages(request):
    msgs = Message.objects.all()
    serial = MessageSerializer(msgs, many=True)
    
    return JsonResponse({'data': serial.data})