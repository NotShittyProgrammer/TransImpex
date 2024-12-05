# # Використовуйте офіційний образ Python з Docker Hub
# FROM python:3.9-slim


# # Встановіть робочий каталог в контейнері
# WORKDIR /app

# # Копіюйте потрібні файли в контейнер
# COPY requirements.txt /app

# # Встановіть залежності
# RUN pip install -r requirements.txt

# # Копіюйте всі файли проекту в контейнер
# COPY . /app

# # Вкажіть команду для запуску вашого веб-сервера
# CMD ["python", "manage_sqllite.py", "runserver", "0.0.0.0:8000"]
# Use the official Python image.
FROM python:3.9

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory.
WORKDIR /app

# Install dependencies.
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project.
COPY . /app/

# Run migrations and collect static files.
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Expose port 8000 and run the app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
