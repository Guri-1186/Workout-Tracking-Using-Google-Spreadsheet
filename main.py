from datetime import datetime
import requests
from dotenv import load_dotenv
import os
load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")
EXERCISE_ENDPOINT = os.getenv("EXERCISE_ENDPOINT")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
GENDER = "female"
WEIGHT_KG = 47
HEIGHT_CM = 166
AGE = 38

headers = {
    "x-app-id":APP_ID,
    "x-app-key" : API_KEY
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

parameters = {
    "query": input("Tell me which exercise you did? "),
    "gender":"female",
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age":AGE
}

response = requests.post(url = EXERCISE_ENDPOINT, json = parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    bearer_headers = {
    "Authorization": f"Bearer {TOKEN }"
    }
    sheet_response = requests.post(
        SHEET_ENDPOINT, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)
       