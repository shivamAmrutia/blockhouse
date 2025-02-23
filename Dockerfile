# Use an official Python image as the base
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the required files
COPY blockhouse/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the app files
COPY blockhouse /app

# Expose the application port
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
