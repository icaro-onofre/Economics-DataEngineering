# Use the official Apache Airflow Docker image
FROM apache/airflow:latest

# Add any additional configurations or dependencies for Airflow, if needed
# For example, you might want to install additional Python packages or system dependencies.
# RUN pip install some-package
# RUN apk add --no-cache some-package

# Set the working directory inside the container
WORKDIR /usr/local/airflow

# Copy your Airflow DAGs and other configuration files to the container's working directory
COPY ./dags /usr/local/airflow/dags
COPY ./config /usr/local/airflow/config

# Define the default command to run when the container starts
CMD ["webserver"]
