FROM python:3.8
WORKDIR /app
COPY main/requirements.txt ./
RUN pip install -r requirements.txt
COPY main/src/mainscript.py /app
COPY main/test/unittesting.py /app
CMD [ "python", "unittesting.py" ]

