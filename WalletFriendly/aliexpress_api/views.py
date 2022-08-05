from django.shortcuts import render
import requests
import json
# Create your views here.

def aliexpress(request):

    url = "https://magic-aliexpress1.p.rapidapi.com/api/products/search"

    user_input = input()
    querystring = {"name": user_input}

    headers = {
	"X-RapidAPI-Key": "b784411f32msh0a213c712d6fc4ap167672jsn30c16b8a59ba",
	"X-RapidAPI-Host": "magic-aliexpress1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    py_data = json.loads(response)
    
    return render(request, '<page_name>.html', {
        'product_name': py_data['docs']['product_title'],
        'product_price' : py_data['docs']['app_sale_price']

        })
