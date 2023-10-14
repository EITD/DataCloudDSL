FROM python:3
WORKDIR /DataCloudDSL
COPY generate_sample_data /DataCloudDSL/generate_sample_data
RUN pip install paho-mqtt
CMD ["python", "/DataCloudDSL/generate_sample_data/generate_sample_data.py"]
