FROM ubuntu:latest
LABEL authors="camil"

ENTRYPOINT ["top", "-b"]