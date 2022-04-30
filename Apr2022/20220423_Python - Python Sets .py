#!!!!!!!!!!!!!由于 Python 中的 set 集合是无序的，所以每次输出时元素的排序顺序可能都不相同。!!!!!!!!!!!!!!!!!!!!!
#并且需要注意的是，数据必须保证是唯一的，因为集合对于每种数据元素，只会保留一份。例如：
#>>> {1,2,1,(1,2,3),'c','c'}
{1, 2, 'c', (1, 2, 3)}
thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


thisset = {"apple", "banana", "cherry"}
print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


set1 = {"abc", 34, True, 40, "male"}
print(set1)


myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)