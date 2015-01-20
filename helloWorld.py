"""SimpleApp.py"""
from pyspark import SparkContext

#logFile = "/Users/AriSharon/spark/spark-1.2.0-bin-hadoop2.4/README.md"  # Should be some file on your system
logFile = "/Users/AriSharon/DScourse/myDataScienceToolBox/kaggleSampleBig"
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print "Lines with a: %i, lines with b: %i" % (numAs, numBs)