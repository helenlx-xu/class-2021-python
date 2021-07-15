s = 'HELLO'
result = s.isalpha()
print(result)

s = '100'
result = s.isdigit()
print(result)

s = 'A1234'
result = s.isalnum()
print(result)

s = ''
result = s.isspace()
print(result)

s = 'HELLO'
result = s.isupper()
print(result)

result = s.islower()
print(result)

flag = True
while flag:
    name = input('用户名/手机号码:')
    if (name.islower() and  name[0].isalpha() and len(name) >= 6) or (name.isdigit() and   len(name) == 11):

        while True:
            password = input('密码:')

            if len(password) == 6 and password.isdigit():

                if (name == 'admin123' or name == '15811119999') and password == '200325':
                    print('用户登录成功! ')
                    flag = False
                    break
                else:
                    print('用户名或者密码有误! ')
                    break
            else:
                print('密码必须是6位数字')
    else:
        print('用户名或者手机号码格式错误! ')