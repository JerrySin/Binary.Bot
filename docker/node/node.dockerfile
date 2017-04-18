# node:latest
FROM        node:6.10.2

MAINTAINER  Jerry Sin

ENV NODE_ENV = production
ENV PORT = 3000

# Copy source code into the image volume
COPY        . /var/www
WORKDIR     /var/www

# VOLUME      ["/var/www", "/logs"]

# RUN         npm install
RUN         ["npm", "install"]

# port to be exposed
EXPOSE      $PORT

ENTRYPOINT  ["npm", "start"]

# Remove the modules before building it
# rimraf node_modules

# Build the image:
# docker build -t trading/node .
# docker build -t trading/node -f node.dockerfile .
# docker build -t trading/node -f node.dockerfile --no-cache .


# Run the image in daemon mode
# docker run -d -p 8080:3000 trading/node