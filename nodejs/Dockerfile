FROM node:20-alpine
WORKDIR /app
COPY package.json /app
RUN npm install
COPY src /app
EXPOSE 3000
CMD ["node", "server.js"]