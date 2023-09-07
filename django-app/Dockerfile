# syntax=docker/dockerfile:1

FROM python:3.11.4-alpine

WORKDIR /usr/src/django-app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install packages
RUN pip install --upgrade pip --quiet
COPY ./requirements.txt .
RUN pip install -r requirements.txt --quiet

EXPOSE 8000

COPY ./entrypoint.sh .

# Link secrets to the app dir
RUN ln -s /run/secrets/django_key ./django_dev_key && ln -s /run/secrets/db_pass ./db_pass_dev

ENTRYPOINT [ "/usr/src/django-app/entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]