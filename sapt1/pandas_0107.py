import pandas as pd

# print(pd.__version__)

# a = [1, 7, 2]
# a = {'x': 1, "y": 7, "z": 2}
# variabila = pd.Series(a, index=['y', 'x', 'a'])
# print(variabila)

data = {
    "key1": [0, 1, 2],
    "key2": [3, 4, 5]
}

variabila = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
# print(variabila.loc[['linie1', 'linie2']])
# print(variabila["key2"]['linie1'])

df = pd.read_csv("test.csv")
# print(df)
df.fillna(888, inplace=True)
# print(df)
# print(df.head(6))
# print(df.tail(6))
# df.loc[7, "AL"] = 45
df.replace(': ', 999, inplace=True)
df.replace(':', 999, inplace=True)
# print(df.transpose())
# df.to_csv('Test.csv')
# df.rename(columns={"AL": "Col_1"}, inplace=True)
# df.rename(index={0: "linie1"}, inplace=True)
# df['CV'] = ['1', 2, 3, 4, 5, 6, 7, 8, 9]
# print(df)
# print(df.describe())
# print(df.mean())

import matplotlib.pyplot as plt
# df['AT'].plot(kind='hist')
# plt.show()

df.plot(kind='scatter', x='AT', y='BE')
# plt.show()
df.corr()
# print(df.corr())