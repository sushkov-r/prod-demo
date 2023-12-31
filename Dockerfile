# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Install the dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Install the project
COPY . .
RUN pip install --no-cache-dir . --no-dependencies

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Uvicorn when the container launches
CMD ["uvicorn", "prod_demo.main:app", "--host", "0.0.0.0", "--port", "8000"]

