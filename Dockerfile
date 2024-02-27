FROM python:3.10.12
WORKDIR /home/otuscub/flask-sqlite3-todo-crud
COPY requirements.txt /home/otuscub/flask-sqlite3-todo-crud
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /home/otuscub/flask-sqlite3-todo-crud
EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0"]