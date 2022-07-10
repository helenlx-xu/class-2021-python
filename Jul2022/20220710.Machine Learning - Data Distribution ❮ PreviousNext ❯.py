import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)#随机数



#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
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

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




#自己写
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 300)
plt.hist(x, 20)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

