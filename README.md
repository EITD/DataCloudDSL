## My Pipeline ##

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

## Example Pipeline ##

### Create MQTT broker ###

In DataCloudDSL directory:

```bash
docker run --name mosquitto -v "$(pwd)/mosquitto_passwd:/mosquitto/config/passwd" -v "$(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf" eclipse-mosquitto
```

> If you use the default configuration file, you will get an Error: Address not available.

### Find mosquitto IP address ###

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
docker run -e MQTT_HOST=172.17.0.2 -e MQTT_CLIENT_ID=publisher -e MQTT_PASS=password eitd/generate_sample_data
```
```bash
docker run eitd/receive_data_from_mqtt
```