FROM python:3
WORKDIR /DataCloudDSL
COPY create_notification /DataCloudDSL/create_notification
RUN pip install paho-mqtt
CMD ["python", "-u", "/DataCloudDSL/create_notification/create_notification.py"]
