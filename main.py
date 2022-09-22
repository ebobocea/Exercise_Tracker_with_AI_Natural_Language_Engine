import requests
from datetime import datetime

APP_ID = "aaa4dab8"
API_KEY = "40510ed79f98e989525b951cf980f9b8"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_params = {
 "query": input("What exercises did you do today?: "),
}
nutritionix_header = {
 "x-app-id": APP_ID,
 "x-app-key": API_KEY,
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_header)
result =  response.json()
sheety_endpoint = "https://api.sheety.co/656241f3d84b9c7f92bef6753783f64c/workoutTracking/workouts"

sheety_header = {"Authorization": "Bearer asjbdnlkansdinwNLKNLKNLKSAdnion1we312or543"}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    new_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

requests.post(url=sheety_endpoint, headers=sheety_header, json=new_data)


