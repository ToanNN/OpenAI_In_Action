from openai import OpenAI
import os

# Read open ai key from environment variable called OpenAIKey
api_key = os.environ.get('OpenAIKey')
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the purpose of life?"},
    ],
)

for choice in completion.choices:
    print(choice.message.content)
    
