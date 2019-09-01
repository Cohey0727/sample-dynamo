FROM node:10.16.3

RUN ["apt-get", "-y", "update"]
RUN ["npm", "install", "dynamodb-admin", "-g"]

EXPOSE 50727
CMD ["dynamodb-admin", "-p", "50727"]