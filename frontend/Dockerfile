FROM node:14-alpine

WORKDIR /code

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 4040

CMD ["npm", "start"]
