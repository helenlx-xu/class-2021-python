list1 = [23,45,77,80,59,10]

def get_list(list_1):
    new_list = [e for e in list_1 if e >= 50]
    print(new_list)


get_list(list1)



def remove_from_list(list_1):
    for e in list_1:
          if e < 50:
                list_1.remove(e)
    print(list_1)

get_list(list1)
