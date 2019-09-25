FROM python:3.7
EXPOSE 5000
ADD run.py /

RUN pip install pystrich
RUN pip install flask



CMD [ "python", "./run.py" ]