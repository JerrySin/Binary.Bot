FROM alpine:3.1

# Update
# RUN apk add --update python py-pip

# Install app dependencies
# RUN pip install Flask

# Bundle app source
COPY collect_R100.py /src/collect_R100.py

# EXPOSE  8000
#CMD ["python", "/src/collect_R100.py", "-p 8000"]
CMD ["python", "/src/collect_R100.py"]