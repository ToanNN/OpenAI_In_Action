# Split the task into multiple tasks
# Moderation
import os, sys
import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_completion import get_completion_from_messages;


delimiter = "####"
system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.
Output a python list of objects, where each object has \
the following format:
    'category': <one of Computers and Laptops, \
    Smartphones and Accessories, \
    Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, 
    Audio Equipment, Cameras and Camcorders>,
OR
    'products': <a list of products that must \
    be found in the allowed products below>

Where the categories and products must be found in \
the customer service query.
If a product is mentioned, it must be associated with \
the correct category in the allowed products list below.
If no products or categories are found, output an \
empty list.

Allowed products: 

Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop
PowerLite Convertible
TechPro Desktop
BlueWave Chromebook

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase
SmartX MiniPhone
MobiTech Wireless Charger
SmartX EarBuds

Televisions and Home Theater Systems category:
CineView 4K TV
SoundMax Home Theater
CineView 8K TV
SoundMax Soundbar
CineView OLED TV

Gaming Consoles and Accessories category:
GameSphere X
ProGamer Controller
GameSphere Y
ProGamer Racing Wheel
GameSphere VR Headset

Audio Equipment category:
AudioPhonic Noise-Canceling Headphones
WaveSound Bluetooth Speaker
AudioPhonic True Wireless Earbuds
WaveSound Soundbar
AudioPhonic Turntable

Cameras and Camcorders category:
FotoSnap DSLR Camera
ActionCam 4K
FotoSnap Mirrorless Camera
ZoomMaster Camcorder
FotoSnap Instant Camera

Only output the list of objects, with nothing else.
"""
user_message_1 = f"""
 tell me about the smartx pro phone and \
 the fotosnap camera, the dslr one. \
 Also tell me about your tvs """
messages =  [  
{'role':'system', 
 'content': system_message},    
{'role':'user', 
 'content': f"{delimiter}{user_message_1}{delimiter}"},  
] 
category_and_product_response_1 = get_completion_from_messages(messages)
print(category_and_product_response_1)

user_message_2 = f"""
my router isn't working"""
messages =  [  
{'role':'system',
 'content': system_message},    
{'role':'user',
 'content': f"{delimiter}{user_message_2}{delimiter}"},  
] 
response = get_completion_from_messages(messages)
print(response)




category_and_product_list = utils.read_string_to_list(category_and_product_response_1)
print(category_and_product_list)
product_information_for_user_message_1 = utils.generate_output_string(category_and_product_list)
print(product_information_for_user_message_1)


system_message = f"""
You are a customer service assistant for a \
large electronic store. \
Respond in a friendly and helpful tone, \
with very concise answers. \
Make sure to ask the user relevant follow up questions.
"""
user_message_1 = f"""
tell me about the smartx pro phone and \
the fotosnap camera, the dslr one. \
Also tell me about your tvs"""
messages =  [  
{'role':'system',
 'content': system_message},   
{'role':'user',
 'content': user_message_1},  
{'role':'assistant',
 'content': f"""Relevant product information:\n\
 {product_information_for_user_message_1}"""},   
]
final_response = get_completion_from_messages(messages)
print(final_response)    