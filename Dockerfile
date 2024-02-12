# Base image
FROM runpod/base:0.4.0-cuda11.8.0

# Install system dependencies (if any)
COPY builder/setup.sh /setup.sh
RUN /bin/bash /setup.sh && \
    rm /setup.sh

# Install Python dependencies
COPY builder/requirements.txt /requirements.txt
RUN python3.11 -m pip install --upgrade pip && \
    python3.11 -m pip install --upgrade -r /requirements.txt --no-cache-dir && \
    rm /requirements.txt

# Add your source code to the Docker image
COPY src /src
WORKDIR /src

# Download the documentation files
RUN python3.11 docs.py

# Set the command to run your application
CMD ["python3.11", "-u", "handler.py"]