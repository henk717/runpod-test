FROM koboldai/koboldcpp
COPY .runpod/handler.py /bin/handler.py
RUN apt update
RUN apt install python3-pip -y
RUN pip install runpod
CMD python3 /bin/handler.py
