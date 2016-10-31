'''
Created on Oct 26, 2016

@author: cris
'''

import os
import paho.mqtt.client as paho
#from publisher import Publisher

class Protocol():
    '''
    classdocs
    '''

    client = paho.Client(client_id="AppPy")
    counter = 0

    def __init__(self):
        '''
        Constructor
        '''
    
    #pub = Publisher()
    
    def on_connect(self, host):
        print("Client ID: " + self.client._client_id + " connected at " + host + ":8883")

    def connect(self, host):
        self.client.on_connect = self.on_connect(host)
        self.client.connect(host, port=8883)      

    def on_subscribe(self, topic):
        print("Subscribed to topic: " + topic)

    def on_message(self, client, userdata, msg):
        data = open("data.txt", "a")
        data.write(msg.payload)
        data.write("\n")
        data.close()
        print ("Received " + msg.payload + ": written on data.txt")
        self.counter += 1
        if self.counter == 6:
            os.system("/home/cris/spark-2.0.1-bin-hadoop2.7/bin/spark-submit spark.py")
            self.counter = 0
            #self.pub.publishCount()
            #count = open("count.txt", "r")
            #count.seek(1,2)
            self.publish("CountsAppPy", "Here I am! :)))")
            #count.close()
            
            
    
    def subscribe(self, topic):
        self.client.on_subscribe = self.on_subscribe(topic)
        self.client.on_message = self.on_message
        self.client.subscribe(topic)
    
    def on_publish(self, client, userdata, mid):
        print("mid: " + str(mid))
        
    def publish(self, topic, string):
        self.client.on_publish = self.on_publish
        (rc, mid) = self.client.publish(topic, string, qos=1)
