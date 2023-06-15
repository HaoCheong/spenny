# Installing the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements into the directory
COPY ./app/requirements.txt /app/

# Install all the python dependency
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Install the dependency for fastapi and sqlalchemy (Not sure if it will be missed)
RUN pip3 install 'fastapi[all]' SQLalchemy

# Execute the uvicorn startup
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
