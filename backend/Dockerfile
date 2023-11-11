# Install python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy the requirement txt into the app
COPY ./app/requirements.txt /app/

# Install all the backend dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Set working directory of the docker container
WORKDIR /

# Debugging entrypoint, keeps container alive to debug
# ENTRYPOINT ["tail", "-f", "/dev/null"]

# Run the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
