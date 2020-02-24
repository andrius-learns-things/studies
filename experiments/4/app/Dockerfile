FROM python:3.8-alpine


# Python app dependencies:
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 5000

CMD ["python", "/code/app.py"]