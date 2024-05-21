FROM python:3.8-slim
WORKDIR /app
COPY order_service.py .
RUN pip install flask requests
CMD ["python", "app.py"]
