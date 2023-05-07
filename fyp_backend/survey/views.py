from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Survey, Question, Answer, Comment
from .serializers import SurveySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class newestSurvey(APIView):
    def get(self, request) -> Response:
        surveys = Survey.objects.all().order_by('-created_at')[:1] # Get the most recent survey
        serializer = SurveySerializer(surveys, many=True)

        return Response(serializer.data)


def index(request) -> render:
    return render(request, 'index.html')

# def view_survey(request, survey_id):
#     survey = Survey.objects.get(pk=survey_id)
#     comments = Comment.objects.filter(survey=survey).select_related('user').order_by('created_at')
#     context = {
#         'survey': survey,
#         'comments': [
#             {
#                 'text': comment.text,
#                 'created_at': comment.created_at,
#                 'username': comment.user.username,
#                 'avatar': comment.user.avatar.url if comment.user.avatar else None,
#             }
#             for comment in comments
#         ],
#     }
#     return render(request, 'view_survey.html', context)

# @api_view(['GET'])
# def get_survey_comments(request, survey_id):
#     survey = Survey.objects.get(pk=survey_id)
#     comments = Comment.objects.filter(survey=survey).select_related('user').order_by('created_at')
#     serializer = CommentSerializer(comments, many=True)
#     return JsonResponse(serializer.data, safe=False)