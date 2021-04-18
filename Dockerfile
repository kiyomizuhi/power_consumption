FROM python:3.8.8

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    ca-certificates \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libffi-dev \
    liblzma-dev \
    libgdm-dev \
    libdb4o-cil-dev \
    libpcap-dev \
    cmake \
    llvm \
    xz-utils \
    tk-dev \
    vim \
    ssh \
    wget \
    curl \
    git \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

ARG workdir
WORKDIR $workdir
