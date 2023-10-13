**Build Image from Dockerfile**

In DataCloudDSL directory:

```bash
docker build -t json_to_txt -f json_to_txt/Dockerfile .
```
```bash
docker build -t translate -f translate/Dockerfile .
```

**Run Container**

In DataCloudDSL directory:

```bash
docker run -v .:/DataCloudDSL json_to_txt
```
```bash
docker run -v .:/DataCloudDSL translate
```