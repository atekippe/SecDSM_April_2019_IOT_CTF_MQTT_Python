import paho.mqtt.client as mqtt
import sched, time

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic")


def on_publish(client, userdata, mid):

    print("Publishing")
    pass


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())
    print(msg.topic)


def on_connect(client, userdata,flags, rc):
    print("Connected to Broker")


def pub_flag():
    client.publish(topic="nothing_here/flag", payload="Go find teacup")


broker = "myothercomputerisyourcomputer.com"
port = 1883
user = "dade"
password = "trashing_our_rights"

client = mqtt.Client("WRITER")
client.on_subscribe  = on_subscribe
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(user, password)

client.connect(broker,port)

starttime=time.time()

while True:
    pub_flag()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))