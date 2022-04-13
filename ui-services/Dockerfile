FROM python:3.7.0
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD ["run.py"]