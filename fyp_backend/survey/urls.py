from django.urls import path
from . import views


urlpatterns = [
    # ... other URL patterns ...
    path('api/survey_comments/<int:survey_id>/', views.get_survey_comments),
]
