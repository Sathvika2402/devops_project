FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask

COPY github.py /github.py

CMD ["python3", "/github.py"]