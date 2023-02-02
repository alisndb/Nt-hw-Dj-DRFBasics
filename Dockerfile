FROM python:3.10

WORKDIR /usr/src/smart_home

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/smart_home
RUN pip install -r requirements.txt

COPY . /usr/src/smart_home

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]