'''
Created on Oct 27, 2016

@author: cris
'''

from pyspark import SparkContext

class Spark(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    sc = SparkContext("local", "Simple App")
    logFile = "Learner.txt"
    logData = sc.textFile(logFile).cache()
    
    print (logData.count())