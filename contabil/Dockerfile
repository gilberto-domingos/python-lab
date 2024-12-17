FROM python:3.12-slim

RUN apt-get update && apt install -y iputils-ping

WORKDIR /application

COPY requirements.txt /application/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

COPY . /application/

ENV ENVIRONMENT=production

CMD ["streamlit", "run", "src/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
