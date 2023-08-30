import ast
import matplotlib.pyplot as plt
import pandas as pd

## Styling a scatterplot
father_son = pd.read_csv("../datasets/father_son.csv")

# Scatterplot 1 - father heights vs. son heights with darkred square markers
plt.scatter(x=father_son.fheight, y=father_son.sheight, c="darkred", marker="p")
plt.show()

# Scatterplot 2 - yellow markers with darkblue borders
plt.scatter(x=father_son.fheight, y=father_son.sheight, c="yellow", edgecolor="darkblue")
plt.show()

# Scatterplot 3
plt.scatter(father_son.fheight, father_son.sheight, c='yellow', edgecolor='darkblue')
plt.grid()
plt.xlabel("father height (inches)")
plt.ylabel("son height (inches)")
plt.title('Son Height as a Function of Father Height')
plt.show()

## Extracting longitude and latitude
df = pd.read_csv("../datasets/test_location.csv", converters={"Location": ast.literal_eval})
print(df.head())

df["lat"] = [loc[0] for loc in df.Location]
df["lng"] = [loc[1] for loc in df.Location]
print(df.head())

##Plotting chickens locations
chickens = pd.read_csv("../datasets/Domesticated_Hen_Permits_clean_adjusted_lat_lng.csv")
print(chickens.head())

plt.scatter(x=chickens.lng, y=chickens.lat)
plt.show()