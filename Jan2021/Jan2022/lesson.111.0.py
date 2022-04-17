n1 = 8
n2 = 5
n3 = 3

result = n1 >= (n2 + n3) and n1 > n2
print(result)

n2 = n2 + n3
result = n1 >= n2 and n1 == n3
print(result)


n4 = (n1 + n3) - n2
result = n4 < n1 and (n4 + n3)>n2
print(result)

username = 'admin123'

email = '63478364@qq.com'

result = username == 'admin123'   or email == '63478364@qq.com'
print(result)

a = 2
b = 5
c = 7

result = (a + b)!= c or c > a
print(result)

flag = False

result = not flag
print('not ---->:',sresult)