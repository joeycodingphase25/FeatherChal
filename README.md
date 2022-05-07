# Overview
This readMe file will cover how to start a local server, a Dockerfile setup, and a docker-compose.yml start up

## Launch Locally with pip and flask, and react

### Create virtual environ in flask-app, and activate
```
$ cd flask-app
$ python3 -m venv venv
$ venv\scripts\activate
$ pip install -r requirements.txt
$ flask run
```
### Start Localhost:3000 with react

```
$ cd react-app
$ npm start
```
------------------------------------------------
## Launch with Dockerfiles in linux
Start docker
```
$ systemctl start docker
$ service docker start
```
Clone files
```
$ git clone https://github.com/joeycodingphase25/FeatherChal.git
$ cd FeatherChal
```
build containers for challengeApp
```
$ docker build -f Dockerfile.flask -t myapp_flask .
$ docker build -f Dockerfile.react -t myapp_react .
$
```
run the containers
```
$ docker run -it -p 5000:5000 myapp_flask:latest
$ docker run -it -p 3000:3000 myapp_react:latest
```
remove when finished
```
$ docker rm -f myapp_flask
$ docker rm -f myapp_react
```
------------------------------------------------
## Launch with Docker-compose
Start docker
```
$ systemctl start docker
$ service docker start
```
Clone files
```
$ git clone https://github.com/joeycodingphase25/FeatherChal.git
$ cd FeatherChal
```
install docker-compose
```
$ apt install docker-compose
$ docker-compose up -d
```
to remove
```
$ docker-compose down
```
