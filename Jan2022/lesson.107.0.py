print('''
**********************
        英雄联盟       
**********************
    ''')

role = input('输入角色:')
equipment = input('输入拥有的装备:')
upgrade_equipment = input('输入想购买装备:')
pay = input('输入付款金额:')

equipment = upgrade_equipment

print('{}拥有{}装备,购买此装备花了{}钱'.format(role,equipment,pay))

print('测试打印升级装备变量:',upgrade_equipment)