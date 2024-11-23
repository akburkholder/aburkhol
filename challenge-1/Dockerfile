FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a

# Challenge metadata and artifacts go here. Only root has access
RUN mkdir /challenge && \
    chmod 700 /challenge

# * Copy jpg with flag to the image
COPY puffin.jpg /app/
WORKDIR /app


RUN tar czvf /challenge/artifacts.tar.gz puffin.jpg && \
    echo "{\"flag\":\"puff1n5_4r3_cu73_TqWy26\"}" > /challenge/metadata.json

CMD ["tail", "-f", "/dev/null"]

