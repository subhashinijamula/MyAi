import json
import requests
import openai
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODVkNGI5NTItZTJiOS00NTY3LTliZDQtMzM4YjBhNmRhYjM0IiwidHlwZSI6ImFwaV90b2tlbiJ9.DIFpKgsgy9NdiS1OwrwzvK-WtEVXU_tMPpuPr-zYynk"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "hi! tell meh a joke..!!",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "hasini"
}
def take(query):
    payload["text"]=query
    # print(payload)
    response = requests.post(url, json=payload, headers=headers)
    # print(response.text)
    result=json.loads(response.text)
    print(result["openai"]["generated_text"])
take("how are you...?")

