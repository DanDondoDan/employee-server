FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /employee_server

# Set the working directory to /music_service
WORKDIR /employee_server

# Copy the current directory contents into the container at /music_service
ADD . /employee_server

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt && \
        python manage.py collectstatic --noinput

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]