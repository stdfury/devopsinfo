FROM python:3.12

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SECRET_KEY=greatsecretkey
ENV DB_HOST=postgres

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "devopsinfo.wsgi:application"]