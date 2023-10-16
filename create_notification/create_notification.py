import paho.mqtt.client as mqtt
import json
import time
import random

# mosquitto ip address
broker_address = "172.17.0.2"
topic = "messages"

# deal with received message
def on_message(client, userdata, message):
    # initing notification directly turns it to a tuple[dict] type ??
    notification = dict()
    notification.update({'notification_type': random.choice(["sms", "email"])})
    notification.update({'message': message.payload.decode()})
    msg = json.dumps(notification)
    client.publish("notifications", msg)
    print(f"Create notification '{msg}'")

# create mqtt client and connect to mqtt broker
client = mqtt.Client()
client.username_pw_set("create_notification", "password")
client.on_message = on_message
client.connect(broker_address, 1883, 60)

# subscribe topic
client.subscribe(topic)

# keep connection
client.loop_start()
time.sleep(30)
client.loop_stop()
