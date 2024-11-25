# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the required Python libraries
RUN pip install requests

# Run the Python script
CMD ["python", "script.py"]
