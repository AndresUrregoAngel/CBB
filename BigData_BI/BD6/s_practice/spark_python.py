from operator import add


fichier = sc.textFile("file:////home/ingenieroandresangel/datasets/BixiMontrealRentals2017/2017/OD_2017-09.csv")
wc = fichier.flatMap(lambda x: x.split(',')).map(lambda x: (x,1)).reduceByKey(add)
wc.saveAsTextFile("file:////home/ingenieroandresangel/datasets/sortiepython")



########################################
#### version script ###########
########################################

from operator import add
from pyspark import SparkContext,SparkConf

conf = SparkConf().setAppName("pyspark").setMaster("yarn-client")
sc = SparkContext(conf=conf)


fichier = sc.textFile("file:////home/ingenieroandresangel/datasets/BixiMontrealRentals2017/2017/OD_2017-09.csv")
wc = fichier.flatMap(lambda x: x.split(',')).map(lambda x: (x,1)).reduceByKey(add)
wc.saveAsTextFile("file:////home/ingenieroandresangel/datasets/sortiepython")
