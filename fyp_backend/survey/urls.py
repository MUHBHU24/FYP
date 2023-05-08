from django.urls import path
from . import views, api
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('myAccount/', api.myAccount, name='myAccount'), # Get user profile
    path('register/', api.register, name='register'), # Register
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Login
    path('surveys/search/', api.search_surveys, name='search_surveys'), # Search surveys
    path('surveys/', api.getAllSurveys, name='getAllSurveys'), # Get the most recent surveys
    # path('/api/surveys/', api.surveys, name='surveys'), # Get all surveys
    path('refresh/', TokenRefreshView.as_view(), name='refreshToken'), # Refresh token
    # path('api/survey_comments/<int:survey_id>/', views.get_survey_comments),
]