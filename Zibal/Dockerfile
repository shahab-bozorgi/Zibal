FROM python:3.12-slim

WORKDIR /app

COPY ./requirements/requirements.txt /app/

RUN pip install --no-cache-dir --no-deps -r /app/requirements.txt

RUN pip install gunicorn==23.0.0

RUN pip install --upgrade pip

RUN pip cache purge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Zibal.wsgi:application"]
