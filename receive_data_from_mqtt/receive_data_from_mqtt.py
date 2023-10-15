import paho.mqtt.client as mqtt

broker_address = "172.17.0.2"
topic = "sample_topic"

# deal with received message
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# create mqtt client
client = mqtt.Client()
client.username_pw_set("subscriber", "password")
client.on_message = on_message

# connect to MQTT Broker
client.connect(broker_address, 1883, 60)

# subscribe topic
client.subscribe(topic)

# listen to messages
client.loop_forever()