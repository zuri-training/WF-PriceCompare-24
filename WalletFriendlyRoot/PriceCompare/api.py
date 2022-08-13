import requests
import json

url = "https://magic-aliexpress1.p.rapidapi.com/api/products/search"

querystring = {"name":"Playstation"}

headers = {
	"X-RapidAPI-Key": "a2f30a74edmsh935c85c0c29ad8bp1c7557jsnc992726fee2b",
	"X-RapidAPI-Host": "magic-aliexpress1.p.rapidapi.com"
	}

response = requests.request("GET", url, headers=headers, params=querystring)


print (response.json())

