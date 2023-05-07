from django.urls import path
from . import views, api
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Login
    path('register/', api.register, name='register'), # Register
    path('my_account/', api.my_account, name='my_account'), # Get user profile
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh token
    # path('api/survey_comments/<int:survey_id>/', views.get_survey_comments),
]