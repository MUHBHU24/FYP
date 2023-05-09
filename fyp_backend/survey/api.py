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
    # Get the most recent surveys first (descending order)
    surveys = Survey.objects.all().order_by('-created_at')
    serializer = SurveySerializer(surveys, many=True)  # can have many surveys

    # safe=False because we are returning a list
    return JsonResponse(serializer.data, safe=False, status=200)


# search function for surveys (used in search bar)
@api_view(['GET'])
def search_surveys(request) -> JsonResponse:
    query = request.GET.get('query')

    # If no query, just return all surveys
    if not query:
        surveys = Survey.objects.all()
    # otherwise, return surveys that match the query
    else:
        surveys = Survey.objects.filter(Q(title__icontains=query))

    serializer = SurveySerializer(surveys, many=True)
    
    return JsonResponse({'surveys': serializer.data}, status=200)


# get survey details for a specific survey (slug)
@api_view(['GET'])
def get_survey_details(request, survey_slug) -> JsonResponse:
    try:
        survey = Survey.objects.get(slug=survey_slug)
        
    except Survey.DoesNotExist:
        return JsonResponse({'error': 'Survey not found'}, status=404)

    question = Question.objects.get(survey=survey)
    answers = Answer.objects.filter(question=question)

    survey_serializer = SurveySerializer(survey)
    question_serializer = QuestionSerializer(question)
    answers_serializer = AnswerSerializer(answers, many=True)

    return JsonResponse({
        'survey': survey_serializer.data,
        'question': question_serializer.data,
        'answers': answers_serializer.data
    }, status=200)


@api_view(['POST'])
def submit_survey(request) -> JsonResponse:
    data = request.data

    try:
        # Assuming the user is authenticated
        user = request.user
        selected_answer = data.get('selected_answer')
        question_id = data.get('question_id')

        # Get the answer and question objects from the database using the ids
        answer = Answer.objects.get(id=selected_answer)
        question = Question.objects.get(id=question_id)

        # Create a new response object and save it to the database
        response = Response.objects.create(user=user, question=question, selected_answer=answer)
        response.save()

        return JsonResponse({'msg': 'Survey submitted successfully'}, status=200)
    
    except Exception as e:
        print("Exception when submitting survey: ", e)

        return JsonResponse({'msg': 'Error when submitting survey'}, status=400)