'''
Created on Oct 26, 2016

@author: cris
'''

from MQTTProtocol import Protocol

if __name__ == '__main__':
    
    mqttPub = Protocol()
    mqttRec = Protocol()
    
    mqttPub.connect("iot.eclipse.org")
    mqttRec.connect("iot.eclipse.org")
    
    mqttRec.subscribe("ProvaString")
    
    mqttPub.client.loop_start()    
    i = 0
    while i < 10:
        mqttPub.publish("ProvaString", "Prova")
        i += 1
    mqttPub.client.loop_stop()
