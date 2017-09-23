CREATE EXTERNAL TABLE bixi
(
STATIONS ARRAY<STRUCT<id: INT,s:STRING,n:string,st:string,b:string,su:string,m:string,lu:string,lc:string,bk:string,bl:string,la:float,lo:float,da:int,dx:int,ba:int,bx:int>>,
SCHEMESUSPENDED STRING,
TIMELOAD TIMESTAMP
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION '/user/ingenieroandresangel/hive/bixihistorical/';

LOAD DATA INPATH '/user/ingenieroandresangel/datasets/bixi2017/Bixi_9_22_9-10.json'
OVERWRITE INTO TABLE bixi;


SELECT 
  temp.id,
  temp.s,
  temp.n,
  temp.st,
  temp.b,
  temp.su,
  temp.m,
  temp.lu,
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
  bixi
  LATERAL VIEW explode(stations) exploded_table as temp
  LIMIT 2;
