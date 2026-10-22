import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('DATA\pj1 mini project.cleaned.csv')
# print(df['price'].describe())
# sns.histplot(data=df,x='rating',bins=10)
# plt.title('Distribution of Ratings')
# plt.xlabel('Ratings')
# plt.ylabel('no. of mobiles')
# # Mobile Price Distribution

# plt.figure(figsize=(8, 5))

# # sns.histplot(data=df, x="price", bins=10)

# # plt.title("Distribution of Mobile Prices")
# # plt.xlabel("Price")
# # plt.ylabel("Number of Mobiles")

# # # Relationship between RAM and Rating

# # plt.figure(figsize=(8, 5))

# # sns.scatterplot(data=df, x="ram", y="rating")

# # plt.title("Mobile RAM vs Rating")
# # plt.xlabel("RAM")
# # plt.ylabel("Rating")

# # # Relationship between Price and Rating

# # plt.figure(figsize=(8, 5))

# # sns.scatterplot(data=df, x="price", y="rating")

# # plt.title("Mobile Price vs Rating")
# # plt.xlabel("Price")
# # plt.ylabel("Rating")

# # Count mobiles by processor
# processor_counts = df["processor"].value_counts().head(10)

# # print(processor_counts)

# # # Visualize the results
# plt.figure(figsize=(10, 5))

# sns.countplot(
#     data=df,
#     y="processor",
#     order=df["processor"].value_counts().head(10).index
# )

# plt.title("Top 10 Most Common Mobile Processors")
# plt.xlabel("Number of Mobiles")
# plt.ylabel("Processor")

# plt.tight_layout()
# plt.show()


print("Dataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


print("Sample prices:")
print(df["price"].head(10).tolist())

print("\nSample storage values:")
print(df["storage"].unique())

print("\nSample RAM values:")
print(df["ram"].unique())

df["price"] = df["price"].str.replace("$", "", regex=False)

df["price"] = pd.to_numeric(df["price"])

print("Cleaned prices:")
print(df["price"].head(10))

print("\nPrice data type:")
print(df["price"].dtype)


def convert_storage(value):
    value = str(value).upper().strip()

    if value.endswith("TB"):
        return float(value.replace("TB", "").strip()) * 1024

    elif value.endswith("GB"):
        return float(value.replace("GB", "").strip())

    else:
        return float(value)


df["storage"] = df["storage"].apply(convert_storage)

print("\nCleaned storage:")
print(df["storage"].unique())

print("\nStorage data type:")
print(df["storage"].dtype)
print("\nUpdated data types:")
print(df.dtypes)

print("\nDataset preview:")
print(df.head())
df.to_csv('DATA\pj1 mini project.finalcleaned.csv', index=False)
