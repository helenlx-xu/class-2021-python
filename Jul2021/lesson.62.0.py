list1 = [i for i in range(1,21)]
print(list1)

list1 = [i+2 for i in range(1,10)]
print(list1)

list1 = [i for i in range(0,101,2)]
print(list1)

list1 = [i for i in range(0,101)]
print(list1)

list1 = []
for i in range(1,21):
    if i%2 == 0:
        list1.append(i)
print(list1)

list1 = [i for i in range(0,101) if i % 2 == 0]
print(list1)

list2 = ['62','hello','100','world','luck','88']

list3 = [word for word in list2 if word.isalpha()]
print(list3)