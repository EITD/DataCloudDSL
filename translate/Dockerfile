FROM python:3.8
WORKDIR /DataCloudDSL
COPY translate /DataCloudDSL/translate
RUN pip install -r /DataCloudDSL/translate/requirements.txt
CMD ["python", "/DataCloudDSL/translate/translate.py"]
