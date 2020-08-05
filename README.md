# NEGOTIATING TRADING PLATFORM

This project has not been completed 100%

Demo URL: http://stock-trading.vlim.co
Alternative Demo URL: http://stock-trading.vlim.co.s3-website-us-east-1.amazonaws.com

## Technologies Involved
* Serverless Application Model
* AWS SNS Service
* AWS API Gateway
* AWS Lambda
* Python3.8
* Docker
* JWT

## Application Description

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI.
The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## To Deploy or Run this application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* AWS CLI - [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

#### To setup local environment, build and deploy your application for the first time:

```bash
# create python virtual environment
$ virtualenv venv -p python3   

# activate the environment you just created
$ source venv/bin/activate

# install all the project python module requirements
$ pip install -r requirements.txt

# build the required external source for deployment
$ sh scripts/layer-build.sh

# change the AWS CREDENTIAL PROFILE and APP_NAME in scripts/config.sh file then run the following in your shell
$ vi scripts/config.sh

# deploy the project
$ sh scripts/deploy.sh
```

#### Run your application locally (http://localhost:3000/) with the `run.sh` command.

```bash
$ sh scripts/run.sh
```

#### To view server log in console, run the following in your shell:

```bash
sh scripts/log.sh resource-function-name

e.g.
sh scripts/log.sh createOrderFunction

```


## Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
$ pip install pytest pytest-mock --user
$ python -m pytest tests/ -v
```

## Cleanup

To delete this application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

To remove stack, run the following in your shell:

```bash
$ sh scripts/remove-stack.sh
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
