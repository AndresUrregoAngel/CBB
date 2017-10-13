
##link to get the jar https://github.com/romainr/cdh-twitter-example#setting-up-hive

set hive.auto.convert.join = false;
ADD JAR /home/cloudera/Downloads/hive-serdes-1.0-SNAPSHOT.jar;


CREATE EXTERNAL TABLE bixi_his
(STATIONS ARRAY<STRUCT<id: INT,s:STRING,n:string,st:string,b:string,su:string,m:string,lu:string,lc:string,bk:string,bl:string,la:float,lo:float,da:int,dx:int,ba:int,bx:int>>,
SCHEMESUSPENDED STRING,
TIMELOAD BIGINT)
ROW FORMAT SERDE 'com.cloudera.hive.serde.JSONSerDe'
LOCATION '/user/cloudera/bixi/dataInput/data_bornes/';



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
CAST(from_unixtime(CAST(CAST(temp.lu as bigint)/1000 as BIGINT), 'dd') AS int) as day_status, 
CAST(from_unixtime(CAST(CAST(temp.lu as bigint)/1000 as BIGINT), 'HH') AS int) as hour_status, 
temp.da,
temp.dx,
temp.ba,
temp.bx
FROM
bixi_his
LATERAL VIEW explode(stations) exploded_table as temp;

SELECT 
sta.s as station_name,
sta.n as station_id,
sta.hour_status,
CAST(AVG(sta.dx)as decimal (10,2)) as places_broken,
CAST(AVG(sta.bx)as decimal (10,2)) as bikes_broken,
CAST(AVG(tr.qty_dp_trips)as decimal (10,2)) as trips_dp,
CAST(AVG(tr.qty_ar_trips)as decimal (10,2)) as trips_ar
FROM
bixi_status_station sta
INNER JOIN bixi_trips_ardp tr
ON sta.n = tr.stationid
AND sta.day_status = tr.day
AND sta.hour_status = tr.hour
GROUP BY sta.s,sta.n,sta.hour_status
ORDER BY trips_dp,trips_ar DESC
LIMIT 100;


