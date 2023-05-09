from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .models import Survey, Question, Answer, Comment
from .serializers import SurveySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import csv



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


# to download survey results as csv
def download_survey_results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    responses = Response.objects.filter(survey=survey)
    response_data = []

    for question in survey.questions.all():
        row = [question.text]
        for choice in question.choices.all():
            row.append(choice.text)
        row.append('Total')
        response_data.append(row)
        for city in User.objects.values_list('city', flat=True).distinct():
            row = [city]
            for choice in question.choices.all():
                count = responses.filter(question=question, selected_choice=choice, city=city).count()
                row.append(str(count))
            row.append(str(responses.filter(question=question, city=city).count()))
            response_data.append(row)
            
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{survey.name}_results.csv"'
    writer = csv.writer(response)

    for row in response_data:
        writer.writerow(row)

    return response