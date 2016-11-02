'''
Created on Oct 26, 2016

@author: cris
'''

from MQTTProtocol import Protocol

ADDRESS = "127.0.0.1"
TOPICSUB = "RandomStringsAppCpp"

class Subscriber(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    mqttPub = Protocol()
       
    mqttPub.connect(ADDRESS)
    mqttPub.subscribe(TOPICSUB)
        
    mqttPub.client.loop_forever()