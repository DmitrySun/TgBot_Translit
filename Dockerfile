FROM python:3.10-slim
ENV TOKEN='7374781289:AAGqWNuCnq7eKZ2xO2KRwvhlPsRqk0vuzLc'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]