from openai import OpenAI
import os

# Read open ai key from environment variable called OpenAIKey
api_key = os.environ.get('OpenAIKey')
client = OpenAI(api_key=api_key)
## Generate an image

response = client.images.generate(
    prompt="Thomas Nguyen a successful and brave entrepreneur like a lion, standing on top of a mountain, looking at the horizon, with a beautiful sunrise in the background.",
    n=2,
    size='1024x1024',
)

for image in response.data:
    print(image.url)