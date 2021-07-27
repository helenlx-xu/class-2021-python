import random
code_list =  set()
s = 'qwertyuiopasdfghjklzxcvbnm1234567890qwertyu8i9opASDFGHJKLZXCVBNM'
while True:
    code = ''
    for i in range (4):
        
        index = random.randint(8,len(s)-1)
        
        code += s[index]
    
    
    code_list.add(code)
    
    
    if len(code_list) == 5:
        break

print(code_list)
