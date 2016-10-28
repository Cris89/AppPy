'''
Created on Oct 27, 2016

@author: cris
'''

from pyspark import SparkContext, SparkConf

class Spark(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        conf = SparkConf().setAppName("Learner").setMaster("local")
        sc = SparkContext(conf=conf)
    
    