from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import MessageSerializer
from .models import Message, Picture
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def create_message(request):
    data = request.data

    print(data)

    return JsonResponse({'message': 'Message was created!'})


# This is the view for the message board. It returns all messages in the database.
@api_view(['GET'])
def all_messages(request):
    msgs = Message.objects.all()
    serial = MessageSerializer(msgs, many=True)
    
    return JsonResponse(serial.data, safe=False)