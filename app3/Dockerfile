FROM python:3.9.19


RUN mkdir /app

WORKDIR /app


# Copy HTML files into the container
COPY ./html ./html

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./scripts/script.py ./script.py

EXPOSE 80

ENTRYPOINT [ "python", "script.py" ]



