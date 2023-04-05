import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "804b6f33d7mshcad781738f3592fp1b3b4djsne4976c33932d",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.json())