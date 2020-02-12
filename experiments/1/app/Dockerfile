FROM python:3.8-alpine

COPY ./requirements.txt /requirements.txt
COPY ./code /code

RUN pip install -r /requirements.txt

EXPOSE 5000

CMD ["python", "/code/app.py"]