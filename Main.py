import requests
import string
import json
alphabet = string.ascii_letters + string.digits + '_{}'
flag = 'spbctf{'
done = False
i = 0
target_dist = 27
while not done:
    for char in alphabet:
        print(flag + char + ' ' * (27 - i) + '}')
        
        r = requests.post('https://cat-step.disasm.me/',{
            'flag': flag + char  + ' ' * (27 - i) + '}'
        })
        dist = json.loads(r.text)
        print(dist)
        if dist['length'] == target_dist:
            break
    
    flag += char
    print(flag)
    target_dist -= 1
    i += 1
