# Use a minimal Node.js image
FROM node:18-alpine 

# Set working directory
WORKDIR /app

# Copy package.json and install serve globally
COPY package.json package-lock.json ./

# Install all the dependencies
RUN npm install

# Expose port 3000
EXPOSE 5173

# ENTRYPOINT ["tail", "-f", "/dev/null"]

# Serve the app
CMD ["npm", "run", "dev", "--", "--host"]