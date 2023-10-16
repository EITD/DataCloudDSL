import paho.mqtt.client as mqtt
import os
import time

# get env variable
mqtt_host = os.environ.get("MOSQUITTO_HOST")
mqtt_client_id = os.environ.get("MOSQUITTO_USERNAME")
mqtt_pass = os.environ.get("MOSQUITTO_PASSWORD")

# mosquitto ip address
broker_address = mqtt_host
topic = "sample_topic"

# deal with received message
def on_message(client, userdata, message):
    msg = message.payload.decode()
    print(f"Receive message '{msg}'")
    client.publish("messages", msg)

# create mqtt client and connect to mqtt broker
client = mqtt.Client()
client.username_pw_set(mqtt_client_id, mqtt_pass)
client.on_message = on_message
client.connect(broker_address, 1883, 60)

# subscribe topic
client.subscribe(topic)

# keep connection
client.loop_start()
time.sleep(20)
client.loop_stop()