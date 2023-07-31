# Use the official dbt Docker image (available on Docker Hub)
FROM dbtlabs/dbt:latest

# Add any additional configurations or dependencies for dbt, if needed
# For example, you might want to install additional dbt packages or tools.
# RUN pip install some-package

# Set the working directory inside the container
WORKDIR /dbt_project

# Copy your dbt project files to the container's working directory
COPY ./dbt_project /dbt_project

# Define the default command to run when the container starts
CMD ["dbt", "run"]
