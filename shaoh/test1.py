# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 00:04:13 2018

@author: Administrator
"""
import pandas as pd
from datetime import datetime
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import seaborn as sns
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 10]
train = pd.read_csv('C:\\Users\Administrator\\Desktop\\train.csv')
test = pd.read_csv('C:\\Users\\Administrator\Desktop\\test.csv')
pd.set_option('display.float_format',lambda x: '%.3f' % x)
train.head()


