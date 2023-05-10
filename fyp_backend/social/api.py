from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponse, JsonResponse
from .serializers import MessageSerializer
from .models import Message
from rest_framework.decorators import api_view

# Create your views here.
 # This is the view for creating a new message. It takes in a POST request with the message data, and creates a new message object.
@api_view(['POST'])
def create_message(request):
    data = request.data
    print(data)
    form = MessageForm(data)

# checks if the form is valid, if it is, it saves the message to the database and returns the message as a JSON object.
    if form.is_valid():
        send = form.save(commit=False)
        userReq = request.user
        send.author = userReq
        send.save()
        serial = MessageSerializer(send)

        return JsonResponse(serial.data, safe=False)

# if the form is not valid, it returns a JSON object with the problem.
    return JsonResponse({'problem': 'something went wrong...'})


# This is the view for the message board. It returns all messages in the database.
@api_view(['GET'])
def all_messages(request):
    msgs = Message.objects.all()
    serial = MessageSerializer(msgs, many=True)
    
    return JsonResponse(serial.data, safe=False)