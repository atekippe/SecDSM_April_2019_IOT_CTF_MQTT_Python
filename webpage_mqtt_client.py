import paho.mqtt.client as mqtt


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic")


def on_publish(client, userdata, mid):

    print("Publishing")
    pass


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload.decode())

    if str(msg.topic) in "the_gibson/haxor":

        #write the incoming mqtt message to file
        i = open("haxors.txt", "a")
        i.write(msg.payload.decode() + "\r\n")
        i.close()

        #read all members in the haxors.txt file

        with open("haxors.txt") as h:
            haxors = h.readlines()
        h.close()

        #write the new index.html - quick and dirty... Yes, I know there is XSS
        f = open("index.html", "w")
        f.write("<!DOCTYPE html>\r\n")
        f.write("<html>\r\n")
        f.write("<body>\r\n")

        f.write("<p>Who has Haxored the Gibson?</p>\r\n")
        f.write("<p>Haxors: </p>\r\n")

        for haxor in haxors:
            f.write("<p>" + haxor.rstrip('\n') + "</p>\r\n")

        f.write("</body>\r\n")
        f.write("</html>\r\n")

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
