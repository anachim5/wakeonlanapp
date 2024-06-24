# Simple Wake on Lan Website
Simple Wake on Lan website to be hosted in the homelab.
Built with Python, Flask and running ansible scripts.
## Install
#### Docker image
Easiest way to run this is to download the image from the docker hub.
```bash
docker run -p 5000:5000 anachim5/wake-on-lan-app 
```
It defaults to the port 5000
#### Build docker file
You can also buila docker image yourself using the Dockerfile.

Clone the repo
```bash
git clone https://github.com/anachim5/wakeonlanapp.git
```

Enter the repo folder
```bash
cd wakeonlanapp
```

Run docker  build command
```bash
docker build -t wakeonlanapp .
```
Run the container 

```bash
docker run -p 5000:5000 wakeonlanapp 
```

#### Run flask app
Flask app can be run by itself.

Clone the repo
```bash
git clone https://github.com/anachim5/wakeonlanapp.git
```

Enter the repo folder
```bash
cd wakeonlanapp
```

Run the flask app (Make sure flask and ansible are installed.)
```bash
pipenv install
```

```bash
python3 app.py
```
