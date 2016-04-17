from django.conf import settings
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from base.utils import NiceChoices
from users.models import User

base_token = 'Harmony@#$753258159'

def get_token_status(request):
    header_name = getattr(settings,'TOKEN','HTTP_TOKEN')
    token = request.META.get(header_name,b'')
    if isinstance(token, type('')):
        # Work around django test client oddness
        token = token.encode(HTTP_HEADER_ENCODING)
    if token:
        if token == base_token:
            return 1, None
        else:
            user = User.objects.filter(secret_key=token).last()
            if user:
                return 2, User

    raise exceptions.AuthenticationFailed

