# Background
-------------

We have to implment a web service which will calculate and provide results for following algorithms vis a REST API:

- Fibonacci:
User will provide valid positive integer - n. The APP will calculate the n-th resilt and reponse in a json format.

Usage: 
curl -X GET "http://localhost:8000/api/v1/algorithms/fibonacci/10" -H  "accept: application/json"

Response:
{ "result": 55 }




- Ackermann function:
User will provide two valid positive integers - m, n. The APP will calculate the value using Ackermann function Alog and reponse in a json format.

Usage: 
curl -X GET "http://localhost:8000/api/v1/algorithms/ackermann/1/2" -H  "accept: application/json"

Response:
{ "result": 4 } 



- Factorial:
User will provide valid positive integer - n. The APP will calculate the factorial and reponse in a json format.

Usage: 
curl -X GET "http://localhost:8000/api/v1/algorithms/factorial/5" -H  "accept: application/json"

Response:
{ "result": 120 }


# Directory Structure

MATHEMATICAL-WEB-SERVICES
    ├── docker-compose.yml
    ├── README.md
    └── project
        ├── app
        │   ├── __init__.py
        │   ├── config.py
        │   ├── cprofiler_decorator.py
        │   ├── main.py
        │   ├── tests
        │   │   ├── __init__.py
        │   │   ├── test_ackermann.py
        │   │   ├── test_factorial.py
        │   │   ├── test_fibonacci.py
        │   │   └── test_main.py
        │   └── algorithms
        │       ├──__init__.py
        │       ├── ackermann.py
        │       ├── factorial.py
        │       └── fibonacci.py
        ├── .dockerignore
        ├── all_messages.log
        ├── Dockerfile
        ├── entrypoint.sh
        ├── logger.yaml
        └── requirements.txt



# Getting started 
------------------
## Containerize APP
Start by ensuring that you have Docker and Docker Compose:

$ docker -v
Docker version 20.10.8, build 3967b7d

$ docker-compose --version
Docker Compose version v2.0.0-rc.2

Build the image:
```shell
docker-compose build
```

Once the build is done, fire up the container
```shell
docker-compose up
```

Swagger UI: http://localhost:8000/docs


## Local Environment Setup
Run this command to create the virtual env folder
``` bash
python3 -m venv venv
```

Then activate the environment
```bash
source venv/bin/activate
```

Move inside the project directory
```bash
cd project
```


Install the required packages
```bash
pip install -r requirements.txt
```


Run the command to spin up the Application
```shell
sh entrypoint.sh
```

## Profiling
A decorator name profile(`@profile`) is used to profile the run time of functions/classes/modules which  is inspired by and modified the profile decorator of Giampaolo Rodola: http://code.activestate.com/recipes/577817-profile-decorator/

The profile decorator doesn't print the results in stdout. Instead, the results are sent to a file. The decorator accepts the following keyword arguments:

output_file (optional, default = None): path of the output file. If not given, the name of the decorated function is used.
sort_by (optional, default = 'cumulative'): sorting criteria that can be a str, SortKey enum, or a tuple/list of those.
lines_to_print (optional, default = None): number of lines to print. If None all the lines are printed.
strip_dirs (optional, default = False): whether to remove the leading path info from file names.


## Logging
When the system started a custom logger will be created and to be passed to subsequent 
modules. To use the logger, for example, refer to `project/app/main.py` on how to
get the logger from arguments and use it in the code. The configuration file consists 4 logging configurations. 
1. LOG_LEVEL - this is the log level to be used for the code
2. LOG_FORMAT - this is the format of the logged message


Currently logging will stream to console output as well as a file.


## Heartbeat API
We are using a separate endpoint to check the application heartbeat. To access the endpoint, 
go to http://localhost:8000/api/v1/heartbeat.

curl -X GET "http://localhost:8000/api/v1/heartbeat" -H  "accept: application/json"


## API Documentation
We have used Fastapi framework which have native support to swagger.
Fastapi provide built-in swagger ui hence please go to http://localhost:8000/docs


## Testing
### Pre-requisites
See Local Environment Setup

### Run Pytest

```shell
pytest 
```

### Run Coverage

```shell
coverage run -m pytest 
```

## Output:
app/tests/test_ackermann.py ...                                         [ 21%]
app/tests/test_factorial.py ...                                         [ 42%]
app/tests/test_fibonacci.py ....                                        [ 71%]
app/tests/test_main.py ....                                             [100%]

============================= 14 passed in 0.73s ==============================

Generate HTML
```shell
coverage html
```

## Deploy to AWS using Helm (EKS Approach)
Here are the basic steps to follow in order to deploy this application to AWS EKS

### Building Docker Image & push to ECR
1. Intall AWS CLI & Configure AWS (“https://awscli.amazonaws.com/AWSCLIV2.pkg" -o)
2. Create ECR Repo using `aws ecr create-repository ...`
3. Login to ECR and get authenticated using `aws ecr get-login ...`
4. Build Docker image using `Docker build ...`
5. Tagging the image using `docker tag ...`
6. Push the Docker Image to AWS ECR using `docker push ...`


### Deploy image to EKS
1. Prepare Helm Chart Yaml 
2. Get the kubectl credentials using `aws eks --region "${AWS_REGION}" update-kubeconfig ...`
3. Deploy to EKS using Helm `helm upgrade --install ...`
4. Done! Should be acceissible through the browser based on the configuration in Helm ingress yaml configuration.

## Deploy to AWS using Serverless Framework(Lambda Approach)
Here are the basic steps to follow in order to deploy this application to AWS Lambda using Serverless framework

### Prepage the Application
1. Setup the app locally (See: Local Environment Setup )
2. Run The app using `sh entrypoint.sh`
3. Goto Swagger UI: http://localhost:8000/docs
4. Test the app by running `pytest`
5. Check the code coverage by running `coverage run -m pytest`
6. Add `mangum` to make the application compatible with Lambda.

### Use serverless framework to deploy the application
1. Install the serverless CLI via npm `npm install -g serverless`
2. Configure serverless with your credentials using `serverless config credentials ...`
3. Create a serverless.yaml
4. create a package.json file to help install js plugins required by serverless Yaml config
5. Install these js plugins by running `npm install`
6. Create custom domain using `sls create_domain ...`
7. Deploy the application using `sls deploy --stage staging ...`

## TODO
- Implement AWS-Xray SDK
- Install & configure Pre commit hook
- Make logger.yaml cached.
