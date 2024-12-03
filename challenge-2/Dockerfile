FROM ubuntu@sha256:e3f92abc0967a6c19d0dfa2d55838833e947b9d74edbcb0113e48535ad4be12a AS challenge

RUN apt-get update && \
    apt-get install -y python3 \
    socat

RUN mkdir /challenge && \
	chmod 700 /challenge

COPY flag.txt /challenge/
COPY check_password.py /challenge/
COPY start.sh /opt/ 
RUN chmod +x /opt/start.sh

WORKDIR /challenge
RUN tar czvf /challenge/artifacts.tar.gz check_password.py && \
	echo "{\"flag\":\"$(cat flag.txt)\"}" > /challenge/metadata.json

COPY check_password.py /app/ 

WORKDIR /app

RUN chmod 600 check_password.py
RUN chmod +rx check_password.py

EXPOSE 5555 
# PUBLISH 5555 AS socat
CMD ["/opt/start.sh"]
