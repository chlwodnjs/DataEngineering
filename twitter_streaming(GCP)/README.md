# ***DataEngineering***
### - GCP 데이터 파이프라인 구축

~~~
docker build -t de_twitter . 
~~~

~~~
gcloud init
~~~

~~~
gcloud auth configure-docker
~~~

~~~
docker tag de_twitter gcr.io/twitterstreaming-335700/tweet 
docker push gcr.io/twitterstreaming-335700/tweet
~~~

<img width="784" alt="tweetimg" src="https://user-images.githubusercontent.com/66864468/147481234-10dfe5e3-736c-4e7e-8681-7a0572df605a.png">


