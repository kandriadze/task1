import pandas as pd
import numpy as np

csv_file_path = "/home/vaso/Downloads/nyc_tlc_yellow_trips_2018_subset_1.csv"

df = pd.read_csv(csv_file_path)

length = df.shape[0]

print(length)

print(df['pickup_datetime'])

from datetime import datetime
print(datetime.utcnow())

# #data obj gardaqmna
# df["pickup_datetime"] = pd.to_datetime(df['pickup_datetime'].str.split('T')[0] , format = "%Y-%m-%d")
# df["dropoff_datetime"] = pd.to_datetime(df['dropoff_datetime'].str.split('T')[0] , format = "%Y-%m-%d")

print('Before')
print(type(df['pickup_datetime'].iloc[0]))


df["pickup_datetime"] = df["pickup_datetime"].apply(lambda x: datetime.strptime(x.split('T')[0], '%Y-%m-%d').date())
df["dropoff_datetime"] = df["dropoff_datetime"].apply(lambda x: datetime.strptime(x.split('T')[0], '%Y-%m-%d').date())
print('After')

print(type(df['pickup_datetime'].iloc[0]))

# elis datoveba
df = df[['pickup_datetime', 'dropoff_datetime']]

print(df.shape)

# #axali velis sheqmna
df['is_two_or_more_days_ride'] = np.where(df['pickup_datetime'] == df['dropoff_datetime'] , 0 , 1)

print(df)
