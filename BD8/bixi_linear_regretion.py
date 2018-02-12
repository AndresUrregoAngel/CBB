import pandas as pn


df_csv = pn.read_csv('C:\\Users\\P928260\\Downloads\\BixiMontrealRentals2017\\2017\\Read\\OD_2017-06.csv',dtype={"user_id": int},low_memory= False,sep=',')
                
 
# data readiness for stations as starting 
df_csv['start_date_dt']= pn.to_datetime(df_csv['start_date'],infer_datetime_format=True)
df_csv['start_day'] = df_csv['start_date_dt'].dt.weekday_name
df_csv['start_hour'] = df_csv['start_date_dt'].dt.hour
df_start = df_csv.drop(df_csv.columns[[0,2,3,4,5,6]],axis=1)
df_start_summ = df_start.groupby(['start_station_code', 'start_day','start_hour']).size().reset_index(name='start_counts')
##print(df_start_summ.head())

# data readiness for stations as ending

df_csv['end_date_dt']= pn.to_datetime(df_csv['end_date'],infer_datetime_format=True)
df_csv['end_day'] = df_csv['end_date_dt'].dt.weekday_name
df_csv['end_hour'] = df_csv['end_date_dt'].dt.hour
df_end = df_csv.drop(df_csv.columns[[0,1,2,4,5,6,7,8,9]],axis=1)
df_end_summ = df_end.groupby(['end_station_code', 'end_day','end_hour']).size().reset_index(name='end_counts')
##print(df_end_summ.head())

df_rowdata = pn.merge(df_start_summ,df_end_summ,left_on= 'start_station_code'#, 'start_day','start_hour'
                      ,right_on= 'end_station_code'#, 'end_day','end_hour'
                      ,how='inner')
#pd.merge(left, right, left_index=True, right_index=True, how='inner');

df_rowdata.head()
