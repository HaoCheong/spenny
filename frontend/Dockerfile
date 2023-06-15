# Pull official base image
FROM node:13.12.0-alpine

# Set working directory
WORKDIR /app

# Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# Install App Dependencies and into Node Modules
COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install react-script@3.4.1 -g

CMD ["npm", "install"]
