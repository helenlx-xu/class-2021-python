
import random

s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
file = input('输入图片文件全称:')

if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
    i = file.rfind('.')
    name = file[:i] 

    if len(name) < 6:
        
        filename = ''
        s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
        for i in range(4):
            index = random.randint(0, len(s) - 1)
            filename += s[index]
        file = filename = file[i:]
    print('成功上传%s文件' % file)
else:
    print('文件格式错误,上传失败!')




import random
filename = ''
s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
for i in range(6):
    index = random.randint(0, len(s) - 1)
    filename += s[index]
print(filename)