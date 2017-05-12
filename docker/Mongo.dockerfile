# connect to it from an application

# $ docker run --name some-app --link some-mongo:mongo -d application-that-uses-mongo



# connect to it via mongo

# $ docker run -it --link some-mongo:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'

