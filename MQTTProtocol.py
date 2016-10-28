'''
Created on Oct 26, 2016

@author: cris
'''

import paho.mqtt.client as paho

class Protocol():
    '''
    classdocs
    '''

    client = paho.Client(client_id="AppPy")  

    def __init__(self):
        '''
        Constructor
        '''  

    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK received with code %d." % (rc))

    def connect(self, host):
        self.client.on_connect = self.on_connect
        self.client.connect(host, port=8883)
        

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        learner = open("Learner.txt", "a")
        learner.write(msg.payload)
        print msg.payload.upper()
    
    def subscribe(self, topic):
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.subscribe(topic)
    
    def on_publish(self, client, userdata, mid):
        print("mid: "+str(mid))
        
    def publish(self, topic, string):
        self.client.on_publish = self.on_publish
        (rc, mid) = self.client.publish(topic, string, qos=1)