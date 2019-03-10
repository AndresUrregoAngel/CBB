sc

val stationsRDD = sc.textFile("file:///home/ingenieroandresangel/datasets/BixiMontrealRentals2015/OD_2015-10.csv")
val wc = stationsRDD.flatMap(line => line.split(","))
val wcred = wc.map(word => (word,1)).reduceByKey((a,b) => a + b)
