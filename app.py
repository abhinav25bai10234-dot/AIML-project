import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def laptop_price_tool():
    # 1. Loading the local dataset
    try:
        df = pd.read_csv('data.csv')
        df.columns = [c.strip().lower() for c in df.columns]
    except:
        print("Error: data.csv not found in this folder.")
        return

    # 2. Selecting features that customers actually care about
    
    features = ['brand', 'processor', 'ram', 'storage', 'gpu', 'spec_rating']
    
    # use columns that actually exist in your file
    valid_features = [c for c in features if c in df.columns]

    # Converting text categories into numeric flags (One-Hot Encoding)
    # This handles Brand, Processor type, and Graphics type
    df_prepared = pd.get_dummies(df, columns=[c for c in valid_features if df[c].dtype == 'O'], drop_first=True)

    # Prepares X (inputs) and y (price)
    X = df_prepared.select_dtypes(include=[np.number]).drop(['price'], axis=1, errors='ignore')
    if 'unnamed: 0' in X.columns:
        X = X.drop('unnamed: 0', axis=1)
    y = df_prepared['price']

    # 3. Training a standard Random Forest model
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    print("\n" + "="*40)
    print("      LAPTOP PRICE CALCULATOR V1.0      ")
    print("="*40)
    print("Dataset loaded. Model is ready for use.")

    # 4. Interactive Customer Interface
    while True:
        print("\nEnter Laptop Specifications Below:")
        try:
            brand = input("Brand (e.g., apple, hp, dell): ").lower().strip()
            cpu = input("Processor (e.g., i5, i7, ryzen 5): ").lower().strip()
            gpu = input("Graphics (e.g., nvidia, intel, amd): ").lower().strip()
            ram = float(input("RAM (GB): "))
            storage = float(input("Storage (GB): "))
            rating = float(input("Condition/Spec Rating (1-100): "))

            # Creating a blank data row
            user_data = pd.DataFrame(0, index=[0], columns=X.columns)

            # Assigning Numbers
            if 'ram' in user_data.columns: user_data['ram'] = ram
            if 'storage' in user_data.columns: user_data['storage'] = storage
            if 'spec_rating' in user_data.columns: user_data['spec_rating'] = rating
            
            # Assigning Categories (Brand, CPU, GPU)
            if f"brand_{brand}" in user_data.columns: user_data[f"brand_{brand}"] = 1
            if f"processor_{cpu}" in user_data.columns: user_data[f"processor_{cpu}"] = 1
            if f"gpu_{gpu}" in user_data.columns: user_data[f"gpu_{gpu}"] = 1
            
            # Calculating Price
            prediction = model.predict(user_data)[0]
            print(f"\n>>> Estimated Retail Price: {round(prediction, 2)}")

        except Exception as e:
            print("\nError: Please enter numbers for RAM, Storage, and Rating.")

        if input("\nCalculate another laptop? (y/n): ").lower() != 'y':
            print("Closing application...")
            break

if __name__ == "__main__":
    laptop_price_tool()