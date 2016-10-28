'''
Created on Oct 26, 2016

@author: cris
'''

from MQTTProtocol import Protocol

class MyClass(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    mqtt = Protocol()
    
    mqtt.connect("127.0.0.1")
    mqtt.subscribe("RandomStringsAppC")
    
    mqtt.client.loop_forever()