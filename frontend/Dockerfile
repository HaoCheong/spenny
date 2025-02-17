FROM node:18-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

# ENTRYPOINT [ "tail", "-f", "/dev/null" ]

ENTRYPOINT [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]