FROM python:3.8-slim
WORKDIR /app
COPY inventory_service.py .
RUN pip install flask
CMD ["python", "inventory_service.py"]
