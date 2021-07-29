list1 = [i for i in range(0,101) if i % 2 == 0]
print(list1)

list2 = ['62','hello','100','world','luck','88']

list3 = [word for word in list2 if word.isalpha()]
print(list3)

list4 = [word.title() if word.starswith('h') else word.upper() for word in list2]
print(list4)

list5 = [(i,j) for i in range(1,3) for j in range(1,3) ]
print(list5)