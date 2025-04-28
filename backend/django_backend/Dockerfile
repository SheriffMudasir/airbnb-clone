# Use the official Python image as a base image
FROM python:3.12.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies needed for psycopg2 (common) and netcat
RUN apt-get update && apt-get install -y \
    libpq-dev \ 
    gcc \
    netcat \
    && apt-get clean && rm -rf /var/lib/apt/lists/*



WORKDIR /app

# Install pipenv
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir pipenv

# Copy dependency definition files first
COPY Pipfile Pipfile.lock ./

# Install project dependencies (including psycopg2-binary which should be in Pipfile)
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the entrypoint script BEFORE the rest of the code
COPY entrypoint.sh /app/entrypoint.sh

# Fix line endings (if needed) and make executable
# Ensure entrypoint.sh is in the same directory as the Dockerfile when building
RUN sed -i 's/\r$//g' /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Copy the rest of the application code
# This assumes your Django project dir ('django_backend') and manage.py
# are in the build context (the outer 'django_backend' dir).
COPY . .

# Set the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]

# Expose the port
EXPOSE 8000

# Default command passed to the entrypoint script
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]