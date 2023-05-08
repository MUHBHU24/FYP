from django.http import JsonResponse
from .forms import registerForm
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Survey, Question, Answer, Comment
from .serializers import SurveySerializer, CommentSerializer, AnswerSerializer, QuestionSerializer, UserSerializer


# Get user profile
@api_view(['GET'])
def myAccount(request) -> JsonResponse:
    # Get user from request object
    user = request.user

    # Return user profile data as JSON
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        # 'city': user.city,
        # 'age': user.age,
        # 'bio': user.bio,
        # 'avatar': user.avatar.url if user.avatar else '',
    })


# Register user
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request) -> JsonResponse:
    data = request.data
    msg = "Success"

    form = registerForm({
        'first_name': data['first_name'],
        'city': data['city'],
        'username': data['username'],
        'password1': data['password1'],
        'password2': data['password2'],
    })

    if form.is_valid():
        form.save()
    else:
        msg = "Error"
        print("Form errors: ", form.errors)  # Print errors to console

    return JsonResponse({'msg': msg})


# Get all surveys (used in home page) recent first
@api_view(['GET'])
def getAllSurveys(request) -> JsonResponse:
    surveys = Survey.objects.all().order_by('-created_at')[:1] # Get the most recent survey
    serializer = SurveySerializer(surveys, many=True) # can have many surveys

    return JsonResponse({'data': serializer.data})


# search function for surveys (used in search bar)
@api_view(['GET'])
def search_surveys(request) -> Response:
    query = request.GET.get('query')

    # If no query, just return all surveys
    if not query:
        surveys = Survey.objects.all()
        serialized_surveys = [survey.serialize() for survey in surveys]
        return Response(serialized_surveys)
    # otheriwse, return surveys that match the query
    elif query:
        surveys = Survey.objects.filter(Q(title__icontains=query))
        serialized_surveys = [survey.serialize() for survey in surveys]
        return Response(serialized_surveys)
    # If no surveys match the query, return an empty list
    else:
        return Response({'surveys': []})