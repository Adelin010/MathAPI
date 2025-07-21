FROM node:alpine

WORKDIR /frontend

# the dest(second param) can be either absolute in the container or 
# relative to the working directory
COPY ./app/package*.json ./

RUN npm install 

COPY ./app ./app

EXPOSE 3000

CMD [ "npm", "run", "dev" ]

