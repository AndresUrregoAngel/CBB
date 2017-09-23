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
  dayofmonth(from_unixtime(CAST(CAST(temp.lu as bigint)/1000 as BIGINT), 'yyyy-MM-dd HH:mm')) as day_month,
  temp.da,
  temp.dx,
  temp.ba,
  temp.bx
FROM
  bixi_his
  LATERAL VIEW explode(stations) exploded_table as temp;
  
# Relation damages by day per station just to ensure a relation between the total damages and the issues per day

  SELECT
    bixidy.n,
    bixidy.s,
    bixidy.day_month,
    SUM(bixidy.dx),
    total_qty.total_dx,
    SUM(bixidy.bx),
    total_qty.total_bx
  FROM 
    bixi_status_station bixidy INNER JOIN  
  (SELECT 
   n,
   s,
   SUM(dx) as total_dx,
   SUM(bx) as total_bx
  FROM 
    bixi_status_station
  GROUP BY n,s) total_qty
ON bixidy.n = total_qty.n
GROUP BY bixidy.n,bixidy.s,bixidy.day_month,total_qty.total_dx,total_qty.total_bx
ORDER BY total_qty.total_dx DESC
LIMIT 20;

# General damages
# Output required
CREATE VIEW bixi_stations_damages
AS
SELECT 
   n,
   s,
   SUM(dx) as total_dx,
   SUM(bx) as total_bx
  FROM 
    bixi_status_station
  GROUP BY n,s
  ORDER BY total_dx DESC
  LIMIT 10;


