import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
df=pd.read_csv(r'DATA\pj1 mini project.finalcleaned.csv')
# Get user preferences 
budget = float(input("Enter your maximum budget: "))
min_ram = int(input("Enter minimum RAM (GB): "))
min_storage = float(input("Enter minimum storage (GB): "))
min_rating = float(input("Enter minimum rating: "))
recommended = df[
     (df["price"] <= budget) & 
     (df["ram"] >= min_ram) & 
     (df["storage"] >= min_storage) &
      (df["rating"] >= min_rating) 
     ]

recommended=recommended.sort_values(
        by='rating',
        ascending=False
     )
if recommended.empty:
    print("No smartphones match your criteria.")
else:
    print("\nRecommended smartphones:")
    print(recommended[["name", "price", "ram", "battery", "storage", "rating"]]
    .head(5).to_string(index=False))
    # Select numerical features for similarity
features = [ "rating", "price", "camera", "display_size", "battery", "storage", "ram", "weight" ]
#Prepare feature data
X = df[features].copy()
  # Convert features to numeric values
X = X.apply(pd.to_numeric, errors="coerce") 
# Remove rows with missing feature values
valid_rows = X.notna().all(axis=1)
X = X.loc[valid_rows] 
phones = df.loc[valid_rows].copy()
 # Scale features so large numbers do not dominate 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X)


 # Train the nearest-neighbors model 
model = NearestNeighbors( n_neighbors=min(6, len(X_scaled)), metric="euclidean" ) 
model.fit(X_scaled) 
print("Machine-learning model is ready!") 
print("Smartphones available:", len(phones))

def recommend_similar_phones(phone_name, number=5):
    # Find the selected smartphone
    matches = phones[
        phones["name"].astype(str).str.lower()
        == phone_name.lower()
    ]

    if matches.empty:
        print("Smartphone not found in the dataset.")
        return

    # Get the selected phone's position in the model data
    phone_index = matches.index[0]
    position = phones.index.get_loc(phone_index)

    # Find similar smartphones
    distances, indices = model.kneighbors(
        [X_scaled[position]],
        n_neighbors=min(number + 1, len(phones))
    )

    print(f"\nPhones similar to {phone_name}:")

    count = 0

    for idx in indices[0]:
        # Do not recommend the selected phone itself
        if phones.iloc[idx]["name"] == phone_name:
            continue

        phone = phones.iloc[idx]

        print(
            f"Name: {phone['name']} | "
            f"Price: {phone['price']} | "
            f"RAM: {phone['ram']} GB | "
            f"Storage: {phone['storage']} GB | "
            f"Rating: {phone['rating']}"
        )

        count += 1

        if count == number:
            break
        
selected_phone = input(
    "\nEnter the smartphone name to find similar phones: "
)

recommend_similar_phones(selected_phone)



