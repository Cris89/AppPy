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
    
    mqtt.connect("iot.eclipse.org")
    mqtt.subscribe("ProvaString")
    
    mqtt.client.loop_forever()