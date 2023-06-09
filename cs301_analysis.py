# -*- coding: utf-8 -*-
"""cs301-analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1odp83aB3kuMgkSSdXSYEGqqzzl60hxGw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os.path import join
import seaborn as sns

from google.colab import drive
drive.mount("./drive")

fname = "cs301values.csv"
path_prefix = '/content/drive/MyDrive/CS301'
df = pd.read_csv(join(path_prefix, fname))

df["Average"] = df.iloc[:, 1:10].mean(axis=1)/10000000
df

my_df = df.iloc[:, [0, 11]]
my_df

my_df = my_df.sort_values("numOfStr")
my_df

x_axis = my_df.iloc[:, 0]
y_axis = my_df.iloc[:, 1]

theta = np.polyfit(x_axis, y_axis, 1)
y_line = theta[1] + theta[0] * x_axis

plt.scatter(x_axis, y_axis)
plt.plot(x_axis, y_line, "r")
plt.title('Performance Testing')
plt.xlabel('Number of Strings')
plt.ylabel('Required Time (nanoTime)')
plt.show()