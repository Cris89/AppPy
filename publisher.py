'''
Created on Oct 26, 2016

@author: cris
'''

from mqttProtocol import Protocol

class Publisher(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    mqttPub = Protocol()
    
    mqttPub.connect("127.0.0.1")
    
    def publishCount(self):
        count = open("count.txt", "r")
        count.seek(1,2)
        self.mqttPub.publish("CountsAppPy", count.readline())