# Install python base image
FROM python:3.9
  
# Set working directory
WORKDIR /app
  
# Copy the requirement txt into the app
COPY ./app/requirements.txt /app/
  
# Install all the backend dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
  
# Install extra fastapi dependencies
RUN pip3 install 'fastapi[all]' SQLalchemy
  
# Run the thing
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]