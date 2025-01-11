# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for mysqlclient and Pillow
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential libjpeg-dev zlib1g-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy all the project files to the container
COPY . /app

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "main.py"]
