'''
Created on Oct 26, 2016

@author: cris
'''

from mqttProtocol import Protocol

class Subscriber(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    mqttPub = Protocol()
    
    mqttPub.connect("127.0.0.1")
    mqttPub.subscribe("RandomStringsAppCpp")
    
    mqttPub.client.loop_forever()