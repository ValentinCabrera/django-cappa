FROM python:3.9

WORKDIR /

COPY . /

EXPOSE 8000

RUN pip3.9 install --no-cache-dir -r requirements.txt

CMD ["python3.9", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
