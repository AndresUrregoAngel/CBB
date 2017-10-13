
##link to get the jar https://github.com/romainr/cdh-twitter-example#setting-up-hive

ADD JAR /home/cloudera/Downloads/hive-serdes-1.0-SNAPSHOT.jar;

CREATE EXTERNAL TABLE bixi_his
(STATIONS ARRAY<STRUCT<id: INT,s:STRING,n:string,st:string,b:string,su:string,m:string,lu:string,lc:string,bk:string,bl:string,la:float,lo:float,da:int,dx:int,ba:int,bx:int>>,
SCHEMESUSPENDED STRING,
TIMELOAD BIGINT)
ROW FORMAT SERDE 'com.cloudera.hive.serde.JSONSerDe'
LOCATION '/user/cloudera/bixi/dataInput/data_bornes/';

