# Use the official Python Docker image
FROM python:3.11.4-bullseye


# Set the working directory inside the container
RUN mkdir -p /App
COPY . /App
WORKDIR /App


RUN pip install --upgrade pip
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install

RUN pip install pandas \
                requests \
                boto3 \
                beautifulsoup4 \
                pyarrow \
                python-dotenv



# Copy your Python application files to the container's working directory


