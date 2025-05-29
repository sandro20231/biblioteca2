# Usa imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Comando padrão (sobrescrevível pelo docker-compose)
CMD ["python", "manage.py", "test"]