import random

def generate_code():
    s = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm'
    code = ''
    for i in range(4):
        r = random.choice(s)
        code += r
    print(code)

print(generate_code)

