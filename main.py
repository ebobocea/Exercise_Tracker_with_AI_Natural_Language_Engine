import requests

APP_ID = "aaa4dab8"
API_KEY = "40510ed79f98e989525b951cf980f9b8"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_params = {
 "query": "ran 3 miles",
}
headers = {
 "x-app-id": APP_ID,
 "x-app-key": API_KEY,
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)

print(response.text)