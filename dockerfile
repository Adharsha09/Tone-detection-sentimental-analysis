FROM python:3.10

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py","--host = 0.0.0.0","--port=5000"]