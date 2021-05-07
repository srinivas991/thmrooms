FROM python:3.5.2-slim
WORKDIR /home/app
COPY cmd_service.pyc /home/app/cmd_service.pyc

RUN pip3 install uncompyle6

CMD ["uncompyle6", "/home/app/cmd_service.pyc"]
# docker build . -t peakhill:decompyle
# docker run peakhill:decompyle