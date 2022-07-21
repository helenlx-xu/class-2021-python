# 80%用于培训，20%用于测试。

# 使用训练集训练模型。

# 使用测试集测试模型。

# 训练模型意味着创建模型。

# 测试模型均值测试模型的准确性。

# 从数据集开始
# 从要测试的数据集开始。

# 我们的数据集展示了一家商店中的100位客户，以及他们的购物习惯。




# 评估模型
# 在机器学习中，我们创建模型来预测某些事件的结果，就像在上一章中，当我们知道重量和发动机尺寸时，我们预测了汽车的二氧化碳排放量。

# 为了衡量模型是否足够好，我们可以使用一种名为Train/Test的方法。

# 什么是训练/测试
# 训练/测试是一种测量模型准确性的方法。

# 它被称为训练/测试，因为您将数据集拆分为两个集：训练集和测试集。
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
#随机





import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 3))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




#自己
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
print(mymodel(5))

