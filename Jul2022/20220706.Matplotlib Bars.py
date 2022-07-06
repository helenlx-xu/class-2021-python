#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')#Matplotlib 是一个 Python 的 2D绘图库

import matplotlib.pyplot as plt#Pyplot 是 Matplotlib 的子库
import numpy as np#NumPy 是一个数学库,与和 Matplotlib（绘图库）一起使用

x = np.array(["A", "B", "C", "D"])#组数array的值
y = np.array([3, 8, 1, 10])

plt.bar(x,y)#柱状图plt.bar()
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)#plt.savefig一个保存图像的函数 sys提供了许多函数和变量来处理 Python 运行时环境的不同部分 stdout
sys.stdout.flush()#flush 刷新缓冲区


#自写
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
