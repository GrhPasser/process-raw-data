# -*- coding: utf-8 -*-
# author: Runhao G
# time: 2021/3/11
import numpy as np

a = np.array([[1, 2, 3]]).T
b = np.array([[2, 3, 4], [3, 4, 5]]).T
c = np.concatenate((a, b), axis=1)
print(c[:, 1:])
