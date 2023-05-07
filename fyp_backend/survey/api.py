from django.http import JsonResponse
from .forms import registerForm
from rest_framework.decorators import authentication_classes, permission_classes, api_view


# Get user profile
@api_view(['GET'])
def my_account(request) -> JsonResponse:
    print('Authorization header:', request.headers.get('Authorization'))

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
