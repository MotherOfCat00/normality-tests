import math
import pandas as pd
import numpy as np
import sys
from scipy.stats import shapiro
from scipy.stats import anderson
from scipy.stats import normaltest
import seaborn as sns
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

path_n = r'D:\magisterka\normokapnia.csv'
normokapnia = pd.read_csv(path_n)  # load data to DataFrame
names = []
for col in normokapnia.columns:  # add headers to list 'names'
    names.append(col)

names.remove('patient')
print(normokapnia.describe())  # print descriptive statiistics

for item in names:
    print(item)
    print(shapiro(normokapnia[item]))  # Shapiro-Wilk test
    print(normaltest(normokapnia[item]))  # D'Agostino test
    AD, crit, sig = anderson(normokapnia[item])  # Anderson test
    # calculate p-value for Anderson test:
    AD = AD * (1 + (.75 / 50) + 2.25 / (50 ** 2))
    if AD >= .6:
        p = math.exp(1.2937 - 5.709 * AD - .0186 * (AD ** 2))
    elif AD >= .34:
        p = math.exp(.9177 - 4.279 * AD - 1.38 * (AD ** 2))
    elif AD > .2:
        p = 1 - math.exp(-8.318 + 42.796 * AD - 59.938 * (AD ** 2))
    else:
        p = 1 - math.exp(-13.436 + 101.14 * AD - 223.73 * (AD ** 2))
    print("statistics=", AD, "Anderson p = ", p)

amp_df = normokapnia[['AMP_spec', 'AMP_ptp', 'AMP_max']]
pi_df = normokapnia[['PI_spec', 'PI_ptp', 'PI_max']]


# boxplots with seaborn
plt.figure()
sns.set(font_scale=1.5)
sns.boxplot(data=pi_df)
sns.stripplot(data=pi_df)

plt.figure()
sns.set(font_scale=1.5)
sns.boxplot(data=amp_df)
sns.stripplot(data=amp_df)

plt.show()
