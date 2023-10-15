FROM python:3
WORKDIR /DataCloudDSL
COPY generate_sample_data /DataCloudDSL/generate_sample_data
RUN pip install paho-mqtt
CMD ["sh", "-c", "echo Echoing the envParam Frequency: $Frequency ; echo Echoing the envParam Duration: $Duration ; echo Echoing the envParam MQTT_HOST: $MQTT_HOST ; echo Echoing the envParam MQTT_CLIENT_ID: $MQTT_CLIENT_ID ; echo Echoing the envParam MQTT_PASS: $MQTT_PASS ; python /DataCloudDSL/generate_sample_data/generate_sample_data.py"]