FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os arquivos necessários para instalar as dependências
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# Copia todo o código-fonte do projeto para o diretório de trabalho, preservando a estrutura
COPY . /app/

# Define a variável de ambiente para produção
ENV ENVIRONMENT=production

# Define o comando de execução do Streamlit
CMD ["streamlit", "run", "src/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
