# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Install the dependencies
COPY pyproject.toml .
# RUN pip install --no-cache-dir .
RUN pip install --no-cache-dir streamlit requests

# Install the project
COPY . .
RUN pip install --no-cache-dir . --no-dependencies

EXPOSE 8501

# Run Uvicorn when the container launches
CMD ["streamlit", "run", "src/prod_demo/ui.py"]
