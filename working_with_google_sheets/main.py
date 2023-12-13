import pandas as pd
import ssl
import pprint
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://docs.google.com/spreadsheets/d/1HhoARjapfXrosE03Kp98SPHmFDKBi_GtKg3RMu7JB78/gviz/tq?tqx=out::csv&sheet=2023"
data = pd.read_csv(url)

for index, row in data.iterrows():
    print(f"Temperature at hour {row['Hour']}: {row['Temperature']}")

# for index, row in data.iterrows():
#     print(row['Year'])