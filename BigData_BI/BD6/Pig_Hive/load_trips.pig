#Go into pig with tez to improve performance and HCatalog to play with hive tables
pig -x tez -useHCatalog

# load trips historical info
trips = LOAD '/user/ingenieroandresangel/datasets/bixitrips/' USING PigStorage(',')
AS (departure_date:chararray,departure_station:chararray,arrival_date:chararray,arrival_station:chararray,duration:long,member:int);



#Cleaning the relation just to play with departure and arrival and get the most frequent

trips_stations = FOREACH trips GENERATE departure_station, arrival_station;
trips_stations_gr = GROUP trips_stations  BY (departure_station, arrival_station);
trips_gr_total = FOREACH trips_stations_gr GENERATE  FLATTEN(group) as (departure:chararray,arrival:chararray) , (int) COUNT(trips_stations) as (qty_trips:int);

trips_srt = ORDER trips_gr_total BY qty_trips DESC;

# top ten trips year 2017
trips_ck = LIMIT trips_srt 10;

## add station name

stations = LOAD '/user/ingenieroandresangel/datasets/Bixi2017.csv' USING PigStorage(',')
AS (code:chararray,name:chararray,la:chararray,lo:chararray);

trips_stations_dep = JOIN trips_srt by departure LEFT OUTER, stations by code;
trips_stations_dep_cl = FOREACH trips_stations_dep GENERATE 
trips_srt::departure as (departure_id:chararray), stations::name as (departure_name:chararray), trips_srt::arrival as (arrival_id:chararray),
trips_srt::qty_trips as (qt_trips:int);

trips_stations_arr = JOIN trips_stations_dep_cl by arrival_id LEFT OUTER, stations by code;
trips_stations = FOREACH trips_stations_arr GENERATE 
trips_stations_dep_cl::departure_id as (departure_id:chararray), trips_stations_dep_cl::departure_name as (departure_name:chararray), trips_stations_dep_cl::arrival_id as (arrival_id:chararray),
stations::name as (arrival_name:chararray), trips_stations_dep_cl::qt_trips as (qt_trips:int);

trips_stations_srt = ORDER trips_stations BY qt_trips DESC;
trips_stations_ck = LIMIT trips_stations_srt 10;

## Store result about the most common trips in 2017 with stations name

STORE  trips_stations_srt INTO '/user/ingenieroandresangel/datasets/bixioutputs/trips_2017/' USING PigStorage (',');
