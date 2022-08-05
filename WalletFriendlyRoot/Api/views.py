
from django.shortcuts import render
import requests


# Create your views here.

# setting up the request parameters
params = {
'api_key': '150B604A39B54860B3FEEF3F64DECAD1',
  'type': 'search',
  'amazon_domain': 'amazon.com',
  'search_term': 'memory cards'
}

def Search(request):
  api_result=requests.get('https://api.rainforestapi.com/request', params)
  return render(api_result)

 