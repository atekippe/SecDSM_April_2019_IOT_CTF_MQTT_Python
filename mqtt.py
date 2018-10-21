import paho.mqtt.client as mqtt
import time
import os
from PIL import Image, ImageDraw
from PIL import ImageFont


def write_image(payload):
    img = Image.new('RGB', (640, 480), color=(0, 0, 0))

    d = ImageDraw.Draw(img)

    font = ImageFont.truetype("Lato-Black.ttf", 32)
    d.text((230, 220), payload, fill=(32, 194, 14), font=font)

    img.save('pil_text.png')
    img.show()


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic")


def on_publish(client, userdata, mid):

    print("Publishing")
    pass


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())
    print(msg.topic)

    if str(msg.topic) in "the_gibson/test":
        print("YES")
        os.system("killall display")
        write_image(msg.payload.decode())

def on_connect(client, userdata,flags, rc):
    print("Connected to Broker")


broker = "myothercomputerisyourcomputer.com"
port = 1883
user = "dade"
password = "trashing_our_rights"




client = mqtt.Client("PWN_ME")
client.on_subscribe  = on_subscribe
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(user, password)

client.connect(broker,port)
client.subscribe(topic="the_gibson/test", qos=0)

client.loop_forever()