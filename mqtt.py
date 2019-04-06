import paho.mqtt.client as mqtt
import time
import os
from PIL import Image, ImageDraw
from PIL import ImageFont


def write_image(payload):
    img = Image.new('RGB', (480, 272), color=(0, 0, 0))

    d = ImageDraw.Draw(img)

    font = ImageFont.truetype("Lato-Black.ttf", 32)
    d.text((150, 100), payload, fill=(32, 194, 14), font=font)

    img.save('pil_text.png')
    #img.show()
    os.system('feh pil_text.png &')

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
        os.system("killall feh")
        write_image(msg.payload.decode())
    if str(msg.topic) in "the_gibson/haxor":
        f = open("index.html", "a")
        f.write(msg.payload.decode() + "\r\n")
        f.close()

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
client.subscribe(topic="the_gibson/#", qos=0)

client.loop_forever()
