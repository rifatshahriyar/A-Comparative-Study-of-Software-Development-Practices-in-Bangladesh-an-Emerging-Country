# Created by Partha at 8/16/19
import pandas as pd
import json

# Step 1 #
# df = pd.read_csv("../Data/MainData.csv")
# rows, columns = df.shape
# df = list(df)
# headers = {df[item]: '' for item in range(0, columns - 1)}
# json.dump(headers, open("../Data/Headers.json", "w"))
# ---------------------------------- #

# Step 2 #
df = pd.read_csv("../Data/MainData.csv")
temp_headers = json.load(open("../Data/Headers.json", "r"))
headers = {}
for key, value in temp_headers.items():
    headers[key] = value['header']
print(headers)
df.rename(columns=headers, inplace=True)
print(df.columns)
