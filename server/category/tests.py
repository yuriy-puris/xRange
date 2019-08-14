# from django.test import TestCase

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Category
from .serializers import CategorySerializer
# Create your tests here.

class BaseViewTest(APITestCase):
  client = APIClient()

  @staticmethod
  def create_song(category_value="", category_url=""):
    if category_value !="" and category_url != "":
      Category.objects.create(category_value=category_value, category_url=category_url)

  

class GetAllCategoryTest(BaseViewTest):

  def test_get_all_category(self):
    expected = Category.objects.all()
    serialized = CategorySerializer(expected, many=True)