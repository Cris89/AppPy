'''
Created on Oct 30, 2016

@author: cris
'''

from pyspark import SparkContext, SparkConf

DATA = "data.txt"
COUNT = "count.txt"

class Spark():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    logFile = DATA
    conf = SparkConf().setAppName("Count").setMaster("local")
    sc = SparkContext(conf = conf)
    logData = sc.textFile(logFile).cache()
    num = str(logData.count())
    
    count = open(COUNT, "a")
    count.write(num)
    count.write("\n")
    count.close()