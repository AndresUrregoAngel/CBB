import pandas as pn
import json
from pandas.io.json import json_normalize


##### get the quantity of bikes required by station

stations_data = open('E:\\Sources\\BixiMontrealRentals2017\\Bixi_info.json','r')
data = json.load(stations_data)
df_stations_all = json_normalize(data['stations'])
df_stations_fl = df_stations_all.drop(df_stations_all.columns[[0,3,4,7,8,9,10,11,12,14,15,16]],axis=1)


df_6002_info = df_stations_fl.where(df_stations_fl['n'] == '6002').dropna(thresh=2)
print(df_6002_info)



#### read the input from the historical repository

df_csv = pn.read_csv('E:\\Sources\\BixiMontrealRentals2017\\OD_2017-06.csv',dtype={"user_id": int},low_memory= False,sep=',')                
 
    
# data readiness for stations as starting 

df_csv['start_date_dt']= pn.to_datetime(df_csv['start_date'],infer_datetime_format=True)
df_csv['start_day'] = df_csv['start_date_dt'].dt.weekday_name
df_csv['start_hour'] = df_csv['start_date_dt'].dt.hour
df_start = df_csv.drop(df_csv.columns[[0,2,3,4,5,6]],axis=1)
df_start_summ = df_start.groupby(['start_station_code', 'start_day','start_hour']).size().reset_index(name='start_counts')
#print(df_start_summ.head())

# data readiness for stations as ending

df_csv['end_date_dt']= pn.to_datetime(df_csv['end_date'],infer_datetime_format=True)
df_csv['end_day'] = df_csv['end_date_dt'].dt.weekday_name
df_csv['end_hour'] = df_csv['end_date_dt'].dt.hour
df_end = df_csv.drop(df_csv.columns[[0,1,2,4,5,6,7,8,9]],axis=1)
df_end_summ = df_end.groupby(['end_station_code', 'end_day','end_hour']).size().reset_index(name='end_counts')
#print(df_end_summ.head())

df_rowdata = pn.merge(df_start_summ,df_end_summ,
                      left_on=['start_station_code', 'start_day', 'start_hour']
                      ,right_on=['end_station_code', 'end_day', 'end_hour']
                      ,how='inner')

df_rowdata_cl = df_rowdata.drop(df_rowdata.columns[[4,5,6]],axis=1)

df_6002 = df_rowdata_cl.where(df_rowdata_cl['start_station_code']==6002 ).dropna(thresh=2)
df_6002
