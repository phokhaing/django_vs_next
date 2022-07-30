FROM python

WORKDIR supportdesk-apps/backend
COPY . .

RUN pip3 freeze > requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /supportdesk-apps/backend/src
CMD python3 manage.py makemigrations \
   && python3 manage.py migrate \
   && python3 manage.py runserver 0.0.0.0:8000
# CMD [ "python3", "manage.py", "makemigrations" ]
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
EXPOSE 8000