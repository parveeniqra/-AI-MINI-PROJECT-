import pandas as pd



df_csv=pd.read_csv('DATA\pj1 mini project.csv')
# print(df_csv.columns)
# print(df_csv.isnull().sum())
# print(df_csv.duplicated().sum())
# print(df_csv.describe(include='all'))
duplicate_count = df_csv.duplicated().sum()
print("Number of duplicate rows:", duplicate_count) 
if duplicate_count > 0:
    print("\nDuplicate records:")
    print(df_csv[df_csv.duplicated(keep=False)]) # Remove only completely identical rows
    df_csv = df_csv.drop_duplicates() 
    print("\nDuplicate rows removed.")
else:
     print("No completely duplicated rows found.")


df_csv.to_csv('DATA\pj1 mini project.cleaned.csv', index=False)
