import paho.mqtt.publish as publish

# mosquitto ip address
broker_address = "172.17.0.2"  
topic = "sample_topic"

# publish message
publish.single(topic, "Hello, DataCloud!", hostname=broker_address)

print("Message published successfully!")