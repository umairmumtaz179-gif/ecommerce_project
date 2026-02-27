import pandas as pd
import matplotlib.pyplot as plt

print("📊 Data Mining Analysis Starting...")

df = pd.read_csv("products.csv")

# Dataset Information
print("\nDataset Info")
print(df.info())

# Average Price
print("\nAverage Price:", df["Price"].mean())

# Top Expensive Products
print("\nTop 5 Expensive Products")
print(df.sort_values("Price", ascending=False).head())

# Rating Distribution
print("\nRating Distribution")
print(df["Rating"].value_counts())

# Price Distribution Graph
plt.figure(figsize=(8,5))
df["Price"].hist()
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Product Price Distribution")
plt.grid()

plt.show()
# Save Analysis Report
with open("analysis_report.txt", "w", encoding="utf-8") as f:

    f.write("E-commerce Data Mining Report\n")
    f.write("=============================\n\n")

    f.write(f"Total Products: {len(df)}\n")
    f.write(f"Average Price: {df['Price'].mean()}\n\n")

    f.write("Rating Distribution:\n")
    f.write(str(df["Rating"].value_counts()))
    
print("✅ Analysis report saved as analysis_report.txt")