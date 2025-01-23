from openai import OpenAI
import os

# Read open ai key from environment variable called OpenAIKey
api_key = os.environ.get('OpenAIKey')
client = OpenAI(api_key=api_key)

def get_completion(prompt, model="chatgpt-4o-latest"):  
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model=model,  
        messages=messages, 
        temperature=0
    )
    
    # Create a list of all message contents
    return [choice.message.content for choice in response.choices]

def get_completion_from_messages(messages, model="chatgpt-4o-latest", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return [choice.message.content for choice in response.choices]
