FROM python:3.9.15-alpine
COPY app /app
RUN pip install -r /app/requirements.txt
CMD ["python","/app/main.py"]
EXPOSE 3000