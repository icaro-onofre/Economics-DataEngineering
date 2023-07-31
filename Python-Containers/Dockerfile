# Use the official Python Docker image
FROM python:3.11.4-bullseye

# Add any additional dependencies for your Python application
# For example, you might want to install specific Python packages.
# RUN pip install some-package

# Set the working directory inside the container
RUN mkdir -p /storage
WORKDIR /App
COPY . .

RUN pip install --upgrade pip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN pip install pandas \
                requests \
                boto3 \
                beautifulsoup4 \
                pyarrow

# Copy your Python application files to the container's working directory




