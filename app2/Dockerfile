FROM python:3.9.19

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./scripts/script.py ./script.py

ENTRYPOINT [ "python", "script.py" ]

