# Use an official Python image as base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only necessary files
COPY t1.py .

# Install dependencies
RUN pip install requests beautifulsoup4

# Set the command to run the script
CMD ["python", "t1.py"]
