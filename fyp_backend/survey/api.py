from django.http import JsonResponse
from .forms import registerForm
from rest_framework.decorators import authentication_classes, permission_classes, api_view


@authentication_classes([])
@permission_classes([])
@api_view(['POST'])
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

    return JsonResponse({'status': msg})