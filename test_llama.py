import requests

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'llama3',
        'prompt': 'Apa itu data science? Jelaskan konsep sederhana'
    },
    stream=False
)
print(response.json()["response"])