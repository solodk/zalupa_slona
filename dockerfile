FROM ubuntu

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app/ 

RUN apt-get update && apt-get install -y && apt-get upgrade -y \
git \
python3 \
python3-pip \
wget \
libxss1 \
libappindicator1 \
libindicator7 \
apt-utils

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i  google-chrome-stable_current_amd64.deb; exit 0
RUN apt --fix-broken install -y
RUN python3 main.py

CMD [ "python3", "./main.py" ]
