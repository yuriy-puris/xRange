import requests
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

