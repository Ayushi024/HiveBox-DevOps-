FROM python:3.9
WORKDIR /app
COPY  app.py .
ENTRYPOINT [ "python","app.py" ]