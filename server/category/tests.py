# from django.test import TestCase

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Category
from .serializers import CategorySerializer
# Create your tests here