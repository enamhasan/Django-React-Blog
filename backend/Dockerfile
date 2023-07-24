FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
