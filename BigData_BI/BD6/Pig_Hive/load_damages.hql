#this command will improve the query performance, tez is a nice feature to avoid go thru map reduce as query engine
set hive.execution.engine=tez; 

#Load historical files coming from the json files
CREATE EXTERNAL TABLE bixi_his
(
STATIONS ARRAY<STRUCT<id: INT,s:STRING,n:string,st:string,b:string,su:string,m:string,lu:string,lc:string,bk:string,bl:string,la:float,lo:float,da:int,dx:int,ba:int,bx:int>>,
SCHEMESUSPENDED STRING,
TIMELOAD BIGINT
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/user/ingenieroandresangel/datasets/bixi2017/';

#checking if the load was completed successfully.
SELECT 
  temp.id,
  temp.s,
  temp.n,
  temp.st,
  temp.b,
  temp.su,
  temp.m,
  temp.lu,
  from_unixtime(CAST(CAST(temp.lu as bigint)/1000 as BIGINT), 'yyyy-MM-dd HH:mm'),
  temp.lc,
  temp.bk,
  temp.bl,
  temp.la,
  temp.lo,
  temp.da,
  temp.dx,
  temp.ba,
  temp.bx,
  schemesuspended,
  timeload
FROM
  bixi_his
  LATERAL VIEW explode(stations) exploded_table as temp;
  LIMIT 2;
  
  
  #Create the table to store the historical data
  
  CREATE TABLE bixi_status_station
  COMMENT 'This table will store only the required fields for the analysis'
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  STORED AS TEXTFILE
  AS 
  SELECT 
  temp.s,
  temp.n,
  from_unixtime(CAST(CAST(temp.lu as bigint)/1000 as BIGINT), 'yyyy-MM-dd HH:mm') as bixi_date,
  CAST(from_unixtime(CAST(CAST(temp.lu as bigint)/1000 as BIGINT), 'HH') AS int) as hour_status, 
  temp.da,
  temp.dx,
  temp.ba,
  temp.bx
FROM
  bixi_his
  LATERAL VIEW explode(stations) exploded_table as temp;
  
# Get AVG damages, qty trips per hour by station top 10
  SELECT 
    sta.s as station_name,
    sta.n as station_id,
    sta.hour_status,
    AVG(sta.dx) as places_broken,
    AVG(sta.bx) as bikes_broken,
    tr.qty_trips 
  FROM
    bixi_status_station sta
  INNER JOIN trips_hour tr
    ON sta.n = tr.departure_station
    AND sta.hour_status = tr.trip_hour
  GROUP BY sta.s,sta.n,sta.hour_status,tr.qty_trips
  ORDER BY tr.qty_trips,places_broken,bikes_broken DESC
  LIMIT 100;

 
 
 
 
