import requests
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.forms import ModelChoiceField
from service_objects.services import Service
from lxml import html
from .models import Category
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response

def get_all_links(res):
    # soup = BeautifulSoup(html, 'lxml')
    page = html.fromstring(res.content)
    print(page)

def main():
    url = 'https://rozetka.com.ua/'
    res_text = get_html(url)
    all_links = get_all_links(res_text)
    return res_text

=======
from bs4 import BeautifulSoup
from lxml import html
import lxml.etree

from .models import Category


class CategoryParser:
    def __init__(self):
      queryset = Category.objects.all()
      url = 'https://elmir.ua/'

    def get_html(self, url):
      response = requests.get(url)
      return response.text

    def get_all_links(self, html):
      pass

    def get_category(self, url):
      html = self.get_html(url)
      timeout = 10
      soup = BeautifulSoup(html, 'lxml')
      print(html)
>>>>>>> 61f010a93dd47c6b72c5c3748c4fb0b1459523fb
