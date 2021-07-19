import pandas as pd
df = pd.read_csv('train.csv', sep=',')
df.to_excel('output.xlsx', 'Sheet1',index=False)


