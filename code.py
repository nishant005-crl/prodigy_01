import pandas as pd
import matplotlib.pyplot as plt

# Simulated population data (in millions)
data = {
    "Country Name": ["India", "USA", "China", "Brazil", "Nigeria"],
    "2013": [1250, 316, 1364, 200, 178],
    "2014": [1267, 318, 1371, 202, 182],
    "2015": [1283, 320, 1378, 204, 186],
    "2016": [1298, 322, 1385, 206, 190],
    "2017": [1312, 324, 1392, 208, 194],
    "2018": [1326, 326, 1399, 210, 198],
    "2019": [1339, 328, 1406, 212, 202],
    "2020": [1353, 331, 1412, 214, 206],
    "2021": [1366, 333, 1418, 216, 210],
    "2022": [1378, 335, 1423, 218, 215],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Melt the data to a long format for easier plotting
df_long = df.melt(id_vars="Country Name", var_name="Year", value_name="Population (Millions)")

# Plot the population distribution in 2022
df_2022 = df_long[df_long["Year"] == "2022"]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df_2022["Country Name"], df_2022["Population (Millions)"], color="skyblue")
plt.title("Population by Country (2022)", fontsize=16)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population (Millions)", fontsize=12)
plt.tight_layout()
plt.show()
