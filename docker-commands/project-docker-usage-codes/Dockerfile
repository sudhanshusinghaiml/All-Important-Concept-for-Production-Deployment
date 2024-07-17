# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# To signify root directory of application
RUN touch /app/.project-root 

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app:USVisaApprovalPredictionapp", "--reload","--host", "0.0.0.0", "--port", "8080"]
