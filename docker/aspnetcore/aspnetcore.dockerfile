FROM        microsoft/aspnet:1.0.0-rc1-update1-coreclr

MAINTAINER  Jerry Sin

COPY        .   /app

WORKDIR     /app

RUN         ["dnu", "restore"]

EXPOSE      5000

ENTRYPOINT  ["dnx", "web"]



# Build the image:
# docker build -t trading/aspnetcore .
# docker build -t trading/aspnetcore -f node.dockerfile .

# Rebuild the image without using cache
# docker build -t trading/aspnetcore -f node.dockerfile --no-cache .

# Run the image in daemon mode
# docker run -d -p 8080:5000 trading/aspnetcore
