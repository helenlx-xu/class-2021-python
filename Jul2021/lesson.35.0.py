s = '小明说：小红你来唱歌吧！小红你来跳舞吧!'
result = s.replace('小红','**',1)
print(result) 

s = '小明 小红 小方'
result = s.split(' ',1)
print(result)

s = '''小明你来唱歌吧！
小红你来跳舞吧！
小方你来学习吧！
小刚你来吃饭吧！
'''
result = s.splitlines()
print(result)