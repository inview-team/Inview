FROM python:3.6

WORKDIR /home/Inview/backend

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b","0.0.0.0:5000", "app"]