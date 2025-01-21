from openai import OpenAI
import os

# Read open ai key from environment variable called OpenAIKey
api_key = os.environ.get('OpenAIKey')
client = OpenAI(api_key=api_key)
## Generate an embedding

response = client.embeddings.create(
    model="text-embedding-3-large",
    input=["Thomas Nguyen is a successful entrepreneur who is brave and has a lion's heart."],
)

print(response)