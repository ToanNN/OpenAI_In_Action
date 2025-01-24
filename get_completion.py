from openai import OpenAI
import os
# from dotenv import load_dotenv, find_dotenv

# _ = load_dotenv(find_dotenv()) # read local .env file

# Read open ai key from environment variable called OpenAIKey
api_key = os.environ.get('OpenAIKey')
client = OpenAI(api_key=api_key)

def get_completion(prompt, model="chatgpt-4o-latest",
                                temperature=0, 
                                 max_tokens=5000):  
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model=model,  
        messages=messages, 
        temperature=temperature,
        max_tokens= max_tokens# degree randomness
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

def get_completion_and_token_count(messages, 
                                   model="gpt-3.5-turbo", 
                                   temperature=0, 
                                   max_tokens=500):
    
    response = client.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    
    content = [choice.message.content for choice in response.choices]
    
    token_dict = {
'prompt_tokens':response['usage']['prompt_tokens'],
'completion_tokens':response['usage']['completion_tokens'],
'total_tokens':response['usage']['total_tokens'],
    }

    return content, token_dict
