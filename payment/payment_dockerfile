FROM python:3.8-slim
WORKDIR /app
COPY payment_service.py .
RUN pip install flask requests
CMD ["python", "payment_service.py"]
