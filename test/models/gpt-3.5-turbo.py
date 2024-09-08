
import os
import openai


# Set OpenAI API Key
# os.environ["OPENAI_API_KEY"]


client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Hacer una solicitud simple
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print("ChatGPT Response:", response.choices[0].message.content.strip())