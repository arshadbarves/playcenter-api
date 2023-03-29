# Setup docker for my Django project

FROM python:3

# Set environment variables 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port
EXPOSE 8000

# Migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run server
CMD ["python", "manage.py", "runserver", "8000"]
