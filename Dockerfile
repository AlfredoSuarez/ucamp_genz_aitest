# Use the official Ubuntu as a parent image
FROM ubuntu:latest AS base

# Set the working directory in the container
WORKDIR /usr/src/app

# Install python and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash python3 python3-pip python3-dev python3-venv curl

RUN python3 -m venv /usr/src/app/venv

# Add activation command to .bashrc
RUN echo "source /usr/src/app/venv/bin/activate" >> /usr/src/app/.bashrc

# Switch to Bash (optional)
SHELL ["/bin/bash", "-c"]

RUN source /usr/src/app/venv/bin/activate

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
# This assumes you have a requirements.txt file listing all dependencies, including Dash and TensorFlow

RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Define environment variable
#ENV NAME GenZ

# Run app.py when the container launches
CMD ["python3", "app.py"]
