# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire application to the container
COPY . .
# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the environment variable to run the Flask app
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]


