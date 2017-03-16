FROM python:2.7.13
MAINTAINER "akanshamehta17@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
CMD ["https://github.com/sithu/assignment1-config-example"]
