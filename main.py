import pandas as pd
import numpy as np

URL = "https://sweeftdigitaltalk.slack.com/files/U02UH39GD0C/F04MPJ6GU1H/nyc_tlc_yellow_trips_2018_subset_1.csv"
df = pd.read_csv(URL)

start_index = 1000
end_index = 2001
rows = df[start_index:end_index]
print(rows)



#data obj gardaqmna
df["pickup_datetime"] = pd.to_datetime(df['pickup_datetime'] , format = "%y%m%d")
df["dropoff_datetime"] = pd.to_datetime(df['dropoff_datetime'] , format = "%y%m%d")

# 2 velis datoveba
df = df(['pickup_datetime'])
df = df(['dropoff_datetime'])
df.to_csv('new_csvfile', index = False)

#axali velis sheqmna
df['is_two_or_more_days_ride'] = np.where(df['pickup_datetime'] == df['dropoff_datetime'] , 0 , 1)
df.to_csv('newer_csvfile' , index = False)

#df.columns = df.columns.str.replace('_', ' ')
