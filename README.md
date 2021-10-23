# ANNHUB Python library

Main backend module, which is used for developing web-app logic and deploying AI model by just a few lines of code.


# Usage

We develop a RESTful web controller into a reusable library between many AI models. With these functionalities: **Input model**, **Define data input**, **logging**, **exception handler**.
## Prerequisite
You should install python 3.7 64bit to run the model from ANSCENTER.
https://www.python.org/downloads/release/python-3710/

## Installing
As we have delivered and managed the library as a [PyPi](https://pypi.org/) package.
You can install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

```bash
$ pip install annhub-python
```
or 
```bash
$ py -m pip install annhub-python
```
## A simple example
```python
from annhub_python import PyAnn

app = PyAnn()

# Define the expected AI model
# We recommend to use relative over absolute path, due to its
# stability in docker engine.
app.set_model(".\TrainedModel_c++.ann")

# Define which model ID will be used
app.set_model_id(5122020)

# Define the input corresponding to the choosen model
app.set_input_length(4)

if __name__ == "__main__":
    app.run()

```
## API 
The library will product two APIs: **health checking**, **predicting** as well as a [Swagger UI](https://swagger.io/) for API documentation.
```
GET: /api/v1/health
POST: /api/v1/predict
```
![Swagger UI](figures/swagger.png)

## Detailed Example

### Local development

We use **Iris Prediction example** to illustrate how to develop a server by using AI model powered by ANNHUB with only few steps. You can use this [link](examples/iris) to access our code.
The procedure of using our library to server AI model is as follows:

 1. Put a trained model into your project folder.
 2. Create main.py file, where some key information will be determined such as model path, model id, input length,...
 3. Run your application by 
 ```
 $ python main.py
 ```
4. With default settings, your AI can be used at [http://localhost:8080](http://localhost:8080). 
You can access [http://localhost:8080/docs](http://localhost:8080/docs) to use your Swagger UI documentation. 
 ### Deployment
 If you want to deliver your AI model as a service, you can follow these steps:

 1. Create Dockerfile to containerize your application. (We recommend to reuse our [Dockerfile](examples/iris/Dockerfile)).
 2. Build your docker image, which contains your AI model.
 ```
 $ docker build --tag <your dockerhub account>/<docker image name>:<your company name-version> .
 ```
 For example:
 ```
 $ docker build --tag anscenterari/iris-ari .
 ```
 3. Login to dockerhub to remote control your application between many servers.
 ```
 $ docker login
 ```
 If you do not have any dockerhub account, you can use ours.
 ```
 username: anscenterari
 password: aihack2021
 ```
 4. Push your docker image to the remote repository (dockerhub)
 ```
 $ docker push <your image tag>
 ```
 For example:
 ```
 $ docker push anscenterari/iris-ari
 ```
 ### On AWS Server
After successfully connected to AWS server, you can follow our instruction to deploy your service.
1. Login to your dockerhub (use an account that you pushed the image).
```
$ docker login
```
2. Pull your image to local server
```
$ docker pull <your image tag>
```
For example
```
$ docker pull anscenterari/iris-ari
```
3. Run your docker image
```
$ docker run -d -p 8080:8080 <your image tag>
```

