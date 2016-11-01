'''
Created on Oct 30, 2016

@author: cris
'''

from pyspark import SparkContext, SparkConf

class spark():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    logFile = "data.txt"
    conf = SparkConf().setAppName("Count").setMaster("local")
    sc = SparkContext(conf = conf)
    logData = sc.textFile(logFile).cache()
    num = str(logData.count())
    
    count = open("count.txt", "a")
    count.write(num)
    count.write("\n")
    count.close()