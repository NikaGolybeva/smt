FROM python:3.7
EXPOSE 5000
ADD run.py /
ADD model.pkl /

RUN pip install numpy
RUN python -m venv venv
RUN venv/bin/pip install numpy

RUN venv/bin/pip install gunicorn
RUN pip install pystrich
RUN pip install flask
RUN pip install pandas
RUN pip install sklearn



CMD [ "python", "./run.py" ]