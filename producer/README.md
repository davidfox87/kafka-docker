```
docker build -t producer .
docker run -v $PWD/configs/test.config:/configs/test.config -it --rm producer bash
```

Run the producer application from within the docker container and then observe the docker-compose logs for the kafka broker

```
python3 ./producer.py

```

