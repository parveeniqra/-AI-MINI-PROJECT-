import pandas as pd
df=pd.read_excel('DATA\pj1 mini project.xlsx')
df.to_csv('DATA\pj1 mini project.csv', index=False)
df_csv=pd.read_csv('DATA\pj1 mini project.csv')
print(df_csv.shape)

print(df.columns.tolist())