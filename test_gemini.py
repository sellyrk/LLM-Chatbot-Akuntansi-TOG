import requests
import json

API_KEY = "AIzaSyA-PtL_L_72-x6pLLaneZMvBtvNnBixqI4"
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=AIzaSyA-PtL_L_72-x6pLLaneZMvBtvNnBixqI4"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Apa fungsi laporan laba rugi pada perusahaan?"
                }
            ]
        }
    ]
}

response = requests.post(URL, headers=headers, json=data)
print(json.dumps(response.json(), indent=2))
