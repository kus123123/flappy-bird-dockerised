FROM ubuntu
RUN apt update && apt install -y python3 python3-pip libglib2.0-0 x11-apps
ENV DISPLAY 192.168.29.1 :0
WORKDIR /app
COPY . /app

RUN pip3 install -r requirement.txt

CMD ["python3", "main.py"]




