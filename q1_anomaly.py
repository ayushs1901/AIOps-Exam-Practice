import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("server_metrics.csv")

# Basic information
print("Total records:", len(df))

print("\nBasic Statistics:")
print(df.describe())

# Detect anomalies
anomalies = df[df["CPU"] > 80]

print("\nAnomalies:")
print(anomalies)

print("\nNumber of anomalies:", len(anomalies))

# Plot CPU usage
plt.plot(df["Timestamp"], df["CPU"], marker="o")
plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Monitoring")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()