FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências do Poetry
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --with dev

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Cria diretório para volume de dados
RUN mkdir -p /data && chmod -R 755 /data

# Executa a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "aplicacao_django.wsgi:application"]
