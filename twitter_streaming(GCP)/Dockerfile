FROM python:3.9-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV GOOGLE_APPLICATION_CREDENTIALS = "/app/twitterstreaming-335700-dfa6120bb104.json"
# Run app.py when the container launches
CMD ["python", "de_twitter.py"]