import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/airline_data.csv")

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# Average price by airline
avg_price = df.groupby("Airline")["Price"].mean()

print("\nAverage Ticket Price by Airline:")
print(avg_price)

# Plotting
plt.figure()
avg_price.plot(kind="bar")
plt.title("Average Ticket Price by Airline")
plt.xlabel("Airline")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
