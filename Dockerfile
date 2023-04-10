FROM ubuntu:latest

WORKDIR /root

ENV LANG C.UTF-8

RUN apt clean
RUN apt update && apt upgrade -y

# apt install
RUN apt install -y zsh git vim curl \ 
    && apt install -y python3 python3-pip \
    && apt install -y ffmpeg

# oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# pip install
RUN pip install --upgrade pydub google-cloud-speech
