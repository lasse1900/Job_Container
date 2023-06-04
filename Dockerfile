# Use the official Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pandoc
RUN apt-get update && apt-get install -y pandoc

# Install pypandoc
RUN pip install pypandoc

# Copy the rest of the app code
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Set the environment variable
ENV FLASK_APP=app.py

# Run the Flask app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
