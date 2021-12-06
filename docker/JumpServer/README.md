# JumpServer 堡垒机

docker run --name jms_all -d \
  -v ${HOME}/docker/jumpserver/core/data:/opt/jumpserver/data \
  -v ${HOME}/docker/jumpserver/koko/data:/opt/koko/data \
  -v ${HOME}/docker/jumpserver/lion/data:/opt/lion/data \
  -p 80:80 \
  -p 2222:2222 \
  -e SECRET_KEY=kWQdmdCQKjaWlHYpPhkNQDkfaRulM6YnHctsHLlSPs8287o2kW \
  -e BOOTSTRAP_TOKEN=KXOeyNgDeTdpeu9q \
  -e LOG_LEVEL=ERROR \
  -e DB_HOST=aio.liukun.com \
  -e DB_PORT=3306 \
  -e DB_USER=jumpserver \
  -e DB_PASSWORD=nu4x599Wq7u0Bn8EABh3J91G \
  -e DB_NAME=jumpserver \
  -e REDIS_HOST=aio.liukun.com \
  -e REDIS_PORT=6379 \
  -e REDIS_PASSWORD=kyUQ9xf7knPbYCQt \
  --privileged=true \
  jumpserver/jms_all:v2.16.3

