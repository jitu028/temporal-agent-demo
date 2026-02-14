
FROM python:3.11-slim
WORKDIR /app
RUN pip install temporalio
COPY worker.py workflow.py ./
CMD ["python","worker.py"]
