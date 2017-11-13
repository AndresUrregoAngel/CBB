//Define the class to map customers coming from the data inputh
case class customer (cusid: Int, name: String, city : String, province: String, postalcode: String)

//spark context
sc
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

//load the file info
val customer_rdd = sc.textFile("file:////home/ingenieroandresangel/scalascripts/customer.txt")
val cusstomerdf = customer_rdd.toDF()

//val def = sqlContext.read.text("/home/ingenieroandresangel/scalascripts/customer.txt")
//df.show()
