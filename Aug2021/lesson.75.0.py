def a(flag):
    if flag:
        print('AAAAAAAAAA') 
    else:
        print('aaaaaaaaaa')
    
    b()


def b():
    print('BBBBBBBBB')




a(True)



#a,b = (1,2)
a,b = get_maxandmin(list1)
print(a,b) 