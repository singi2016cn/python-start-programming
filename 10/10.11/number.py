"""喜欢的数字"""

import json

favorite_number = input('请输入你最喜欢的数字:\n')
filename = 'number.json'
try:
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
except FileNotFoundError:
    pass


try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    pass
else:
    print(favorite_number)
