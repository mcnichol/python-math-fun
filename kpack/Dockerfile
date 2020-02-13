FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  vim \
  git

COPY . /app
ENTRYPOINT ["/app"]
