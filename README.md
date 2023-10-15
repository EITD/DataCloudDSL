# Task1 Pipeline #

### Build Image from Dockerfile ###

In DataCloudDSL directory:

```bash
docker build -t eitd/json_to_txt -f json_to_txt/Dockerfile .
```
```bash
docker build -t eitd/translate -f translate/Dockerfile .
```

### Run Container ###

In DataCloudDSL directory:

```bash
docker run -v .:/DataCloudDSL eitd/json_to_txt
```
```bash
docker run -v .:/DataCloudDSL eitd/translate
```


# Task2 Argo #

Submit argo_task2.yml to argo.


# Task3 DataCloud #

TODO: For Task1 pipeline, can't add `volume` parameter to the outside structure of generated `yml`.


# Task4 Pipeline #

## Repeat Task1 ##

### Create MQTT broker ###

In DataCloudDSL directory:

```bash
docker run --name mosquitto -v "$(pwd)/mosquitto_passwd:/mosquitto/config/passwd" -v "$(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf" eclipse-mosquitto
```

> If you use the default configuration file, you will get an Error: Address not available.

### Find broker IP address ###

Clients need this value when connecting to the broker.

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mosquitto
```

### Build Image from Dockerfile ###

In DataCloudDSL directory:

```bash
docker build -t eitd/generate_sample_data -f generate_sample_data/Dockerfile .
```
```bash
docker build -t eitd/receive_data_from_mqtt -f receive_data_from_mqtt/Dockerfile .
```

### Run Container ###

In DataCloudDSL directory:

```bash
docker run -e Frequency=9 -e Duration=9 -e MQTT_HOST=172.17.0.2 -e MQTT_CLIENT_ID=publisher -e MQTT_PASS=password eitd/generate_sample_data
```
```bash
docker run -e MOSQUITTO_HOST=172.17.0.2 -e MOSQUITTO_USERNAME=subscriber -e MOSQUITTO_PASSWORD=password eitd/receive_data_from_mqtt
```

> MQTT_HSOT should be equal to the broker IP address stated above.

## Repeat Task2 ##

Submit argo_task4.yml to argo.

## Repeat Task3 ##
