FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /local_library
COPY requirements.txt /local_library/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]