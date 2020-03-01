FROM node:13.8-alpine

# Python app dependencies:
COPY ./package.json /package.json
RUN npm install

EXPOSE 5000

CMD ["npm", "run debug"]