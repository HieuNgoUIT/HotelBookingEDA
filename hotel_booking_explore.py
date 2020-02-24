import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sns.set(color_codes=True)

hotel_data = pd.read_csv('hotel_bookings.csv')
hote_data_count = len(hotel_data)
print("hotel data row:" + str(hote_data_count))

hotel_data_succcess = hotel_data[hotel_data['is_canceled'] == 0]
hotel_data_succcess_count = len(hotel_data_succcess)
print("hotel data that not canceled:" + str(hotel_data_succcess_count))
print("% that succeed:" + str(hotel_data_succcess_count /hote_data_count *100 ))

#check what months has the biggest arrival

#print(hotel_data_succcess.arrival_date_month.unique())
biggest_arrival_month= hotel_data_succcess.arrival_date_month.value_counts()
print(biggest_arrival_month)



#print(hotel_data.lead_time.head())

#sns.distplot(a= hotel_data.lead_time, kde=False )
#sns.boxplot(x= hotel_data.lead_time)
#plt.show()
#print(data.columns)
#print(data.sample(5))