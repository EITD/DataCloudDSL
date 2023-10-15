FROM python:3
WORKDIR /DataCloudDSL
COPY receive_data_from_mqtt /DataCloudDSL/receive_data_from_mqtt
RUN pip install paho-mqtt
# -u: force the stdout and stderr streams to be unbuffered
CMD ["sh", "-c", "echo Echoing the envParam MOSQUITTO_HOST: $MOSQUITTO_HOST ; echo Echoing the envParam MOSQUITTO_USERNAME: $MOSQUITTO_USERNAME ; echo Echoing the envParam MOSQUITTO_PASSWORD: $MOSQUITTO_PASSWORD ; python -u /DataCloudDSL/receive_data_from_mqtt/receive_data_from_mqtt.py"]
