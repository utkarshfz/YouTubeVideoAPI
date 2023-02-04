FROM python:3.10
WORKDIR /YouTubeVideoAPI
COPY . /YouTubeVideoAPI
RUN pip3 install -r requirements.txt 
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["application.py"]