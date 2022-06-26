# Use the Python 3.10.2 container image
FROM python:3.10.2

# Set the working directory to /app
WORKDIR /market

# Copy the current directory contents into the container at /app
ADD . /market

# Install the dependencies
RUN pip install -r requirements.txt

# Run the command to start uWSGI
CMD ["Python", "run.py"]