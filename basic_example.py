import os
from dotenv import load_dotenv
load_dotenv()

import requests
import json


API_KEY = os.getenv("OPENAI_API_KEY") 


MAX_TOKENS = 50
TEMPERATURE = 1
old_response = []

def chatgpt_query(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": MAX_TOKENS,  # Corrected key name
        "temperature": TEMPERATURE,
        "model": "gpt-4o"
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        r_json = response.json()
        return r_json["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"


while True:
    prompt = input("Enter your query (or type 'exit' to quit): ").strip()
    
    if prompt.lower() == "exit":
        print("Goodbye!")
        break
    
    response = chatgpt_query(prompt)
    print("\nChatGPT:", response, "\n")
