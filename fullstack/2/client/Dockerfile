FROM node:13.8-alpine

RUN npm install --quiet --global @vue/cli

RUN mkdir /code
COPY . /code

WORKDIR /code/items-app-frontend

RUN npm install

CMD npm run serve
