choice = int(input('\n1.借书 \n2. 还书 \n3.查询 \n4.查看所有 \n5.退出\n请选择你需要的服务: '))
if choice == 1:
    print('借书')
if choice == 2:
    print('还书')
if choice == 3:
    choice_chaxun = input('查询人物(1)or作者(2):')
    if choice_chaxun == '1':
        print('请选择你要查询的书名')
    elif choice_chaxun == '2':
        print('请选择你要查询的作者名')
    else:
        print('你打错了')