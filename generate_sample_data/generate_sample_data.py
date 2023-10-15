import paho.mqtt.client as mqtt
import os
import time

# get env variable
frequency = os.environ.get("Frequency")
duration = os.environ.get("Duration")
mqtt_host = os.environ.get("MQTT_HOST")
mqtt_client_id = os.environ.get("MQTT_CLIENT_ID")
mqtt_pass = os.environ.get("MQTT_PASS")

# mosquitto ip address
broker_address = mqtt_host
topic = "sample_topic"

# create mqtt client and connect to mqtt broker
client = mqtt.Client()
client.username_pw_set(mqtt_client_id, mqtt_pass)
client.connect(broker_address, 1883)

# keep connection
client.loop_start()
time.sleep(int(duration))
client.loop_stop()

# publish messages
for i in range(int(frequency)):
    client.publish(topic, f"Message {i+1}")

print("Message published successfully!")