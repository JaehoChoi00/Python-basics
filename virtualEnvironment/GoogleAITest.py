import os
from google import genai

client = genai.Client()
print("Gemini AI Chatbot Initialized. Type 'end' to exit.\n")
chat = client.chats.create(model="gemini-3.6-flash")

while True:
    user_input = input("User: ")
    if user_input.lower() == 'end':
        break

    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}\n")
