def login(username, password):
    if username == 'admin' and password == '1234':
        print('登录成功')
        return True
    else:
        print('用户名或者密码有误!')
        return False

login('')