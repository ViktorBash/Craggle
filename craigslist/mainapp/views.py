from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models
import requests
from requests.compat import quote_plus


# Requests.compat quote_plus takes a str and converts it into a url ex: hi bob --> hi+bob or %hi+bob%
# Create your views here.
def home(request):
    return render(request, 'base.html')


BASE_CRAIGSLIST_URL = 'https://newjersey.craigslist.org/search/?query={}'


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    # print(search)
    # print(quote_plus(search))

    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    # print(final_url)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features="html.parser")
    post_titles = soup.find_all('a', {'class': 'result-title'})
    print(post_titles)
    # print(data)
    stuff_for_frontend = {'search': search,
                          }
    return render(request, 'mainapp/new_search.html', stuff_for_frontend)

