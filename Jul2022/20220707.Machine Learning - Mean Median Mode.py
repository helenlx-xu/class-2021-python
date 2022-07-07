import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)



import numpy# numpy是Python 语言的一个扩展程序库

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)





from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)#找出出现次数最多的数 和出现的次数


#自己写
import numpy

speed = [1,2,3]

x = numpy.mean(speed)#求平均值

print(x)



import numpy

speed = [1,1,2,5,6,3,4]

x = numpy.median(speed)#求中间数

print(x)



from scipy import stats

speed = [1,2,3,4,5,3,2,3]

x = stats.mode(speed)

print(x)