from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponse, JsonResponse
from .serializers import MessageSerializer
from .models import Message, Upvote
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


# rewritten upvote function with the one below this, kept as backup
# @api_view(['POST'])
# def upvote(request, primary_key):
#     msg = Message.objects.get(id=primary_key)
#     # print(msg.upvote.filter(upvoter=request.user))
#     # print(msg)
#     if not msg.upvote.filter(upvoter=request.user):
#         upvote = Upvote.objects.create(upvoter=request.user)

#         msg= Message.objects.get(id=primary_key)
#         msg.upvoteCount += 1
#         print(msg.upvoteCount)
#         msg.upvote.add(upvote)
#         msg.save()

#         return JsonResponse({'show upvote status': 'this has been upvoted!'})
#     else:
#         return JsonResponse({'show upvote status': 'you have already upvoted this message!'})


@api_view(['POST'])
def upvote(request, primary_key):
    try:
        msg = Message.objects.get(id=primary_key)

        # Check if the user has already upvoted this message
        has_upvoted = msg.upvote.filter(upvoter=request.user).exists()

        # If the user has not upvoted this message
        if not has_upvoted:
            upvote = Upvote.objects.create(upvoter=request.user)
            msg.upvote.add(upvote)
            msg.upvoteCount += 1
            print(msg.upvoteCount)
            msg.save()

            return JsonResponse({'UpvoteStatus': 'This has been upvoted!'})
        else:
            return JsonResponse({'UpvoteStatus': 'You have already upvoted this message!'})
    
    except Message.DoesNotExist:
        return JsonResponse({'error': 'Message not found!'}, status=404)
 