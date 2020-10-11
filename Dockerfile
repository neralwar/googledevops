FROM python:3.8
WORKDIR /project
COPY main/src /project/src
COPY main/test /project/test
COPY requirements.txt .
COPY Dockerfile .
COPY cloudbuild.yaml .

CMD [ "python", "/project/test/unittesting.py" ]



