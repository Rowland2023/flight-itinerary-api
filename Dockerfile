FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install flask flasgger
EXPOSE 5000
CMD ["python", "app.py"]
