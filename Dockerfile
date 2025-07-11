FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Instala sqlite3 e bash
RUN apt-get update && \
    apt-get install -y sqlite3 bash && \
    apt-get clean

# Copia os arquivos do projeto
COPY . .

# Instala dependências do Poetry
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --with dev

# Cria diretório para volume de dados
RUN mkdir -p /data && chmod -R 755 /data

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
