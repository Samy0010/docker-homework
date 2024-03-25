FROM python:3.9.19

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

