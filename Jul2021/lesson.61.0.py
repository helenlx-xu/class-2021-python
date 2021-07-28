choice = int(input('\n1.借书 \n2. 还书 \n3.查询 \n4.查看所有 \n5.退出\n请选择你需要的服务: '))
if choice == 1:
    print('借书')
if choice == 2:
    while Flag1:
        name = input('请输入你要还的书名:')
        author = input('请输入你要还的书的作者:')
        for book in books:
            if name == book['name'] and author == book['author']:
                book['number'] += 1
                Flag1 = False
                break
        else:
            print('书名或作者输入有误，请重新输入：')
if choice == 3:
    choice_chaxun = input('查询人物(1)or作者(2):')
    if choice_chaxun == '1':
        print('请选择你要查询的书名')
    elif choice_chaxun == '2':
        print('请选择你要查询的作者名')
    else:
        print('你打错了')
