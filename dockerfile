FROM python:3.10

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Create the /app directory and set ownership
RUN mkdir /app && chown appuser:appuser /app

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies as root
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code and set ownership
COPY --chown=appuser:appuser . .

# Switch to the non-root user
USER appuser

# Expose the port
EXPOSE 8080

# Set the command to run the application
CMD ["python", "./main.py"]