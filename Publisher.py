'''
Created on Oct 26, 2016

@author: cris
'''

from MQTTProtocol import Protocol
import time

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
    
    mqtt.client.loop_start()
    time.sleep(1)
    
    while True:
        str = raw_input("Enter your string: ");
        mqtt.publish("ProvaString", str)
        time.sleep(1)