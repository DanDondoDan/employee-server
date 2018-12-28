from employee_server import models
from employee_server  import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from employee_server.serializers.user import UserCreateSerializer
from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from django.conf import settings
import datetime
from django.utils import timezone
from employee_server.settings import TOKEN_LIFETIME
from rest_auth.views import LoginView as DrfLoginView
import json
from employee_server.models.user import User


class CustomUser(views.APIView):
    '''
    Create token that expires every 24hrs
    Used for registration in users
    '''

    queryset = models.User.objects.all()
    serializer_class = serializers.UserCreateSerializer

    @property
    def get_serializer(self):
        return serializers.UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                user = serializer.validated_data['email']
                token, created = Token.objects.get_or_create(user=serializer.instance)
                utc_now = timezone.now()
                if token.created == (utc_now - datetime.timedelta(hours=TOKEN_LIFETIME)):
                    token = Token.objects.create(user=serializer.instance)
                    token.created = datetime.datetime.utcnow() + timedelta(hours=TOKEN_LIFETIME)
                    token.save()
        return Response({'token': token.key, 'id': token.user_id})

class LoginView(DrfLoginView):
    
    def dispatch(self, *args, **kwargs):
        request = args[0]
        email, password = None, None
        if request.method == 'POST':
            body = json.loads(request.body.decode())
            email = body['email']
            password = body['password']

        a = super().dispatch(*args, **kwargs)

        if a.status_code != 200 and request.method == 'POST' and email and password.is_valid():
            
            u = User.objects.filter(email=email).first()

            a.status_code = 200
            a.data = serializers.UserPrivateSerializer(u).data

        return a

    def get_response(self):
        serializer_class = serializers.UserPrivateSerializer

        serializer = serializer_class(
            instance=self.user,
            context={'request': self.request}
        )

        return Response(serializer.data)
