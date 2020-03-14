FROM python:3.8-alpine


# This is needed for psycopg2 to work
# https://stackoverflow.com/a/12037133
# https://stackoverflow.com/a/42224405

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

# Python app dependencies:
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 5000

CMD ["python", "/code/app.py"]