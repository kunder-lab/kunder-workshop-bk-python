FROM python:3-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_ENV=development
CMD [ "python", "app.py" ]