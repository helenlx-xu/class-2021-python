def decorater(func):
    def wrapper():
        func()
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')

    return wrapper

@decorater
def house():
    print('毛坯房....')

@decorater
def xxx():
    print('xxxxxx')

house()






def decorater(func):
        print('-------------------->')

        def wrapper():
            func()
            print('刷漆')
            print('铺地板')
            print('买家具')
            print('精装修房子')

        print('-------------------->')
        return wrapper

@decorater
def house():
    print('毛坯房....')


house()