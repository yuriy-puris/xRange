import requests
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
