import pandas as pn
import json
from pandas.io.json import json_normalize


#### read the input from the historical repository

df_csv6 = pn.read_csv('E:\\Sources\\BixiMontrealRentals2017\\OD_2017-06.csv',dtype={"user_id": int},low_memory= False,sep=',')
df_csv7 = pn.read_csv('E:\\Sources\\BixiMontrealRentals2017\\OD_2017-07.csv', dtype={"user_id": int},low_memory= False,sep=',' )
df_csv8 = pn.read_csv('E:\\Sources\\BixiMontrealRentals2017\\OD_2017-08.csv',dtype={"user_id": int},low_memory= False,sep=',')

csv = [df_csv6, df_csv7 , df_csv8]
df_csv = pn.concat(csv)

#print(df_csv['start_date'].head())


# data readiness for stations as starting 

df_csv['start_date_dt']= pn.to_datetime(df_csv['start_date'],infer_datetime_format=True)
df_csv['start_day'] = df_csv['start_date_dt'].dt.weekday_name
df_csv['start_hour'] = df_csv['start_date_dt'].dt.hour
df_csv['start_month'] = df_csv['start_date_dt'].dt.month
df_start = df_csv.drop(df_csv.columns[[0,2,3,4,5,6]],axis=1)
df_start_summ = df_start.groupby(['start_station_code', 'start_month','start_day','start_hour']).size().reset_index(name='start_counts')
#print(df_start_summ.head())

# data readiness for stations as ending

df_csv['end_date_dt']= pn.to_datetime(df_csv['end_date'],infer_datetime_format=True)
df_csv['end_day'] = df_csv['end_date_dt'].dt.weekday_name
df_csv['end_hour'] = df_csv['end_date_dt'].dt.hour
df_csv['end_month'] = df_csv['end_date_dt'].dt.month
df_end = df_csv.drop(df_csv.columns[[0,1,2,4,5,6,7,8,9]],axis=1)
df_end_summ = df_end.groupby(['end_station_code', 'end_month','end_day','end_hour']).size().reset_index(name='end_counts')
#print(df_end_summ.head())

df_rawdata = pn.merge(df_start_summ,df_end_summ,
                      left_on=['start_station_code', 'start_month','start_day', 'start_hour']
                      ,right_on=['end_station_code', 'end_month','end_day', 'end_hour']
                      ,how='inner')

df_rawdata_cl = df_rawdata.drop(df_rawdata.columns[[5,6,7,8]],axis=1)
df_rawdata_cl.columns = ['StationCode','Month','Day','Hour','DepartureQty','ArrivalQty']
df_rawdata_cl['Add/Remove'] = df_rawdata_cl['ArrivalQty'] - df_rawdata_cl['DepartureQty']

df_rawdata_cl.head() 
