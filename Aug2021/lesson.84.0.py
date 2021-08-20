def decorater(func):
    def wrapper(*args,**kwargs):
        r = func(*args,**kwargs)
        print('预计装修费用是:{}元'.format(r))
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')
        return 60000

    return wrapper

@decorater
def house():
    print('我是一个毛坯房...')
    return 50000

r = house()
print(r)


def outer_chek(time):
    print('------------>1')
    def check_time(action):
        print('------------->3')
        def do_action():
            if time < 22:
                return action()
            else:
                return '对不起,您不具有该权限'
        print('--------------->4')
        return do_action
    print('-------------->2')
    return check_time


@outer_check(23)
def play_game():
    return '玩儿游戏'
