import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from get_completion import get_completion

response = get_completion('Please reverse the word: """lillipop"""')

print (response)

## 1 token = 0.75 word

