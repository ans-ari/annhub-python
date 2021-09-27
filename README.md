# backend-module

Main backend module, which is used for developing web-app logic and deploying AI model.

# Usage - Phase 1
**Step 1:** 
Install and update [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

**Step 2:**
Put the desired model into your app with the following path:
```
ml\model\<model_name>
```
**Step 3:** 
Config model name as an environment variable in **.env** file.

**Step 4:**
Build and run docker
```
$ docker-compose build
$ docker-compose up -d
```

# Usage - Phase 2

We develop a RESTful web controller into a reusable library between many AI models. With these functionalities: **Input model**, **Define data input**, **logging**, **exception handler**.

## Installing
Delivering and versioning as a [PyPi](https://pypi.org/) package.
Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):

```
$ pip install annhub-python
```
## A simple example
```python
from annhub_python import PyAnn

pyann = PyAnn()

# Define the expected AI model
pyann.set_model("D:\ARI\ANSCENTER\TrainedModel_c++.ann")

# Define which model ID will be used
pyann.set_model_id(5122020)

# Define the input corresponding to the choosen model
pyann.set_input_length(4)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = False)

```

## API 
The library will product two APIs: **health checking**, **predicting** as well as a [Swagger UI](https://swagger.io/) for API documentation.
```
GET: /api/v1/health
POST: /api/v1/predict
```
![Swagger UI](figures/swagger.png)