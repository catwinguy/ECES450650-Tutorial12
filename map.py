import matplotlib.pyplot as plt
import random

with open('Galaxy3-MetaPhlAn2_on_data_2.metaphlan_species.txt') as f:
    lines = f.readlines()
    # random.shuffle(lines)
    print(lines)
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]
x = x[:5]
y = y[:5]
print(x)
print(y)


# plt.plot(x, y)
# plt.show()

import pandas as pd

df = pd.DataFrame({'species': x,
                   'abundance': y})

df.transpose().to_csv('file.csv')

