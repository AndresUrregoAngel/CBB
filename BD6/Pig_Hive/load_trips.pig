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

order_by_data = ORDER student_details BY age DESC;
