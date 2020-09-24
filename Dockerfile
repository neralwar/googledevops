FROM python:3.8
WORKDIR /app
COPY main/requirements.txt ./
RUN pip install -r requirements.txt
COPY main /app
CMD [ "python", "mainscript.py" ]

