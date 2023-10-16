import logging
import paho.mqtt.client as mqtt
import time
import json

# configure log
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# mosquitto ip address
broker_address = "172.17.0.2"
topic = "notifications"

# deal with received message
def on_message(client, userdata, message):
    msg = message.payload.decode()
    notification_data = json.loads(msg)
    notification_type = notification_data.get("notification_type")
    if notification_type == "email":
        logging.info(f"Filtered email notification '{notification_data.get('message')}'")
        

# create mqtt client and connect to mqtt broker
client = mqtt.Client()
client.username_pw_set("create_notification", "password")
client.on_message = on_message
client.connect(broker_address, 1883, 60)

# subscribe topic
client.subscribe(topic)

# keep connection
client.loop_start()
time.sleep(40)
client.loop_stop()