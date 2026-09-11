# Dockerfile para delivery-service
FROM python:3.12-slim

# Evitar la creación de archivos .pyc y permitir que los logs salgan directamente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema requeridas para PostgreSQL y compilaciones
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . /app/

# Exponer el puerto del microservicio
EXPOSE 8002

# Comando por defecto para iniciar el microservicio
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
