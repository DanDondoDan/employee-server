import logging

from rest_framework import serializers
from employee_server import models


logger = logging.getLogger(__name__)


class UserPublicSerializer(serializers.ModelSerializer):
    pass



