msg = input('发表一句话:')
print('-'*50)
print('以下为回复内容:')
flag = True
while flag:
    #输入用户名:
    username = input('用户名:')
    while True:
        #输入回复内容:
        comment = input('评论:')
        comment = comment.strip()
        #验证内容:
        if len(comment)!= 0:
            #验证长度是否超出20个字：
            if len(comment)<=20:
                #是否存在敏感词汇
                comment.replace('丑陋','**')
                print('\t{}发表的评论是:\n\t{}'.format(username,comment))
                print('回答成功!')
                flag = False
                break
            else:
                print('不能超出20字!')   
        else:
            print('评论内容不能为空!')
    #成功则发出评论,否则重新输入
    