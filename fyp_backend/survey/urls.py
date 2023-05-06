from django.urls import path
from . import views, api
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', api.register, name='register'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/survey_comments/<int:survey_id>/', views.get_survey_comments),
]