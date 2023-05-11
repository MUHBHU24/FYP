from django.shortcuts import render
from .forms import MessageForm
from django.http import HttpResponse, JsonResponse
from .serializers import MessageSerializer, PictureSerializer, ExpandMessageSerializer, ReplySerializer
from .models import Message, Upvote, Picture
from rest_framework.decorators import api_view
from django.core.files.images import get_image_dimensions

# BACKUP api_view for create_message 
# This is the view for creating a new message. It takes in a POST request with the message data, and creates a new message object.
# @api_view(['POST'])
# def create_message(request):
#     data = request.data
#     print(data)
#     form = MessageForm(data)

#     # checks if the form is valid, if it is, it saves the message to the database and returns the message as a JSON object.
#     if form.is_valid():
#         send = form.save(commit=False)
#         userReq = request.user
#         send.author = userReq
#         send.save()
#         serial = MessageSerializer(send)

#         return JsonResponse(serial.data, safe=False)

#     # if the form is not valid, it returns a JSON object with the problem.
#     return JsonResponse({'problem': 'something went wrong...'})


@api_view(['POST'])
def create_message(request):
    data = request.data
    form = MessageForm(data)

    if form.is_valid():
        send = form.save(commit=False)
        userReq = request.user
        send.author = userReq

        # handle image upload
        if 'pic' in request.FILES:
            pic = request.FILES['pic']
            try:
                width, height = get_image_dimensions(pic)
            except TypeError:
                return JsonResponse({'problem': 'uploaded file is not an image'})

            picture = Picture()
            picture.pic = pic
            picture.author = userReq
            picture.save()
            send.messagePic = picture

        send.save()
        serial = MessageSerializer(send)

        return JsonResponse(serial.data, safe=False)

    return JsonResponse({'problem': 'something went wrong...'})


# This is the view for the message board. It returns all messages in the database.
@api_view(['GET'])
def all_messages(request):
    msgs = Message.objects.all()
    serial = MessageSerializer(msgs, many=True, context={'request': request})
    
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
def sendReply(request, id):
    msg = Message.objects.get(id=id)
    data = request.data
    print(request.data)
    data['replier'] = request.user.id
    data['reply'] = msg.id
    serializer = ReplySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'replyStatus': 'this has been replied!'})


@api_view(['POST'])
def upvote(request, id):
    try:
        msg = Message.objects.get(id=id)

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
 

@api_view(['GET'])
def expandMessage(request, id):
    msg = Message.objects.get(id=id)
    serial = MessageSerializer(msg, many=True, context={'request': request})
    
    return JsonResponse(serial.data, safe=False)

