from employee_server import models
from employee_server import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, views
import datetime
from django.utils import timezone
from employee_server.settings import TOKEN_LIFETIME


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
