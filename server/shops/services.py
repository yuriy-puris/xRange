import requests
from bs4 import BeautifulSoup
from lxml import html

from .models import Shops

def save():
  poll = Shops(shop_url="https://eldorado.ua/")
  poll.save()