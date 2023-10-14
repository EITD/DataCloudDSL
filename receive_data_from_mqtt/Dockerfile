FROM python:3
WORKDIR /DataCloudDSL
COPY receive_data_from_mqtt /DataCloudDSL/receive_data_from_mqtt
RUN pip install paho-mqtt
# -u: force the stdout and stderr streams to be unbuffered
CMD ["python", "-u", "/DataCloudDSL/receive_data_from_mqtt/receive_data_from_mqtt.py"]
