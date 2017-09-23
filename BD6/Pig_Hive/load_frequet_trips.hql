CREATE EXTERNAL TABLE bixi_his
(
STATIONS ARRAY<STRUCT<id: INT,s:STRING,n:string,st:string,b:string,su:string,m:string,lu:string,lc:string,bk:string,bl:string,la:float,lo:float,da:int,dx:int,ba:int,bx:int>>,
SCHEMESUSPENDED STRING,
TIMELOAD BIGINT
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/user/ingenieroandresangel/datasets/bixi2017/';


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
  LATERAL VIEW explode(stations) exploded_table as temp
  LIMIT 2;
  
  
  
