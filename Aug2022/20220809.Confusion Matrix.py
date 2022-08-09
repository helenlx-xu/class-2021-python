#混淆矩阵

# TP(True Positive)：将正类预测为正类数，真实为0，预测也为0
# FN(False Negative)：将正类预测为负类数，真实为0，预测为1
# FP(False Positive)：将负类预测为正类数， 真实为1，预测为0
# TN(True Negative)：将负类预测为负类数，真实为1，预测也为1
#在机器学习领域中，混淆矩阵（confusion matrix）是一种评价分类模型好坏的形象化展示工具
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

