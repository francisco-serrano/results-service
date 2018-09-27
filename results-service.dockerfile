FROM python:3.6

ENV FLASK_APP app.py
ENV FLASK_ENV development
ENV FLASK_DEBUG 0

WORKDIR /app

RUN mkdir -p /app/data/raw

ADD ./app.py /app/
ADD ./database_utils.py /app/
ADD ./properties.py /app/
ADD ./requirements.txt /app/
ADD ./ResultsDatabase.py /app/
ADD ./data/results.db /app/data/
ADD ./data/raw/* /app/data/raw/

RUN pip install -U -r requirements.txt

EXPOSE 8081

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8081"]