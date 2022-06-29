import matplotlib# matplotlib:绘图库
print(matplotlib.__version__)#version:版本




#Three lines to make our compiler able to draw:
import sys#sys:系统
import matplotlib
matplotlib.use('Agg')#agg = aggregate agg其实就是调用apply函数

import matplotlib.pyplot as plt#pyplot:脚本层  plt:绘图格式文件
import numpy as np#numpy:Numeric Python”，它是 Python 的第三方扩展包，主要用来计算、处理一维或多维数组。  np:“numpy”库

xpoints = np.array([0, 6])#array:数组
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)#plot:绘制一维曲线的基本函数
plt.show()#显示

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)#savefig:保存绘制数据后创建的图形  buffer缓冲器
sys.stdout.flush()#stdout:标准输出 (stdout) 指的就是在命令行里，每次你输入指令后，终端上打印出来的那些话，那些反馈
#flush描述Python 文件 flush() 方法是用来把文件从内存buffer(缓冲区)中强制刷新到硬盘中，同时清空缓冲区

