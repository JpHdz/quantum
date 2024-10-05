# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install Python packages
RUN pip install --upgrade pip
RUN pip install qiskit flask flask-cors docker numpy

# Copy the local Flask app (app.py) to the container
COPY . /app

# Set the default command to run when the container starts
CMD ["python", "app.py"]