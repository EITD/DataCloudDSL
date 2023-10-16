FROM python:3
WORKDIR /DataCloudDSL
COPY filter_notification /DataCloudDSL/filter_notification
RUN pip install paho-mqtt
CMD ["python", "-u", "/DataCloudDSL/filter_notification/filter_notification.py"]
