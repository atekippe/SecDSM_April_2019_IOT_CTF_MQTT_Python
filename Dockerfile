FROM python:3
ADD webpage_mqtt_client.py /
ADD haxors.txt /
RUN pip3 install paho-mqtt
RUN apt-get update
RUN apt-get install apache2 -y
ADD index.html /var/www/html/


