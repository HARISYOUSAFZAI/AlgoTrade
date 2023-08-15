# it will use python 3.9 version
FROM python:3.9 
# copying the current forlder under the name of /app
COPY . /app
#here are using /app folder where we copied our files 
WORKDIR /app
#  we run this file to install all the libraries to support our program
RUN pip install -r requirements.txt
# this port will be given by the Heroku
EXPOSE $PORT
# this command is used for the flask and gunicorn only supports linus operating system,
# workers means there will be four listener four your project
#  app:app means file_name:flask_name
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
