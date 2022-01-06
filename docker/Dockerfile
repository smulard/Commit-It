FROM python:3.7

WORKDIR /app 

# enough for pip install, so there's an image layer checkpoint to speed up builds
COPY requirements.txt /app

COPY . . 

RUN git clone https://github.com/smulard/Commit-It.git

CMD ["sleep 10000"]

#ENTRYPOINT [ "python3" ]

#CMD ["commit.py", "--shomer"]