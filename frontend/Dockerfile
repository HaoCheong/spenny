  
# Pull official base image
FROM node:13.12.0-alpine
  
# Set working directory
WORKDIR /app
  
# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH
  
# install app dependencies and into node_modules/
COPY package.json ./
COPY package-lock.json ./
COPY yarn.lock ./
RUN npm install react-scripts@3.4.1 -g
RUN npm install
# RUN yarn install
  
# Add all the contents from directory
#COPY . ./
# EXPOSE 8000
# Start app
# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["npm", "start"]
