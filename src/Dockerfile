FROM python:3.8
RUN mkdir -p /usr/src/itunes
WORKDIR /usr/src/itunes
COPY . /usr/src/itunes
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3","main.py"]

