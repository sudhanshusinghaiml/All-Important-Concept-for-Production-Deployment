# =======================================================================================================
# Steps that I should follow to create docker image locally
# =======================================================================================================
https://levelup.gitconnected.com/the-essential-guide-to-using-docker-in-machine-learning-and-data-science-77f2a12395cb

# 1. Initialize the docker in the repository.
docker init

<<COMMENT
docker init
Welcome to the Docker Init CLI!

This utility will walk you through creating the following files with sensible defaults for your project:
  - .dockerignore
  - Dockerfile
  - compose.yaml
  - README.Docker.md

Let's get started!

? What application platform does your project use? Python
? What version of Python do you want to use? 3.11.4
? What port do you want your app to listen on? 5000
? What is the command to run your app? python3 -m flask run --host=0.0.0.0
COMMENT


# 3. To build docker image using the Dockerfile on local system.
# Go to the project directory and run the below command from Docker Quickstart Toolbox
docker build -t banking-loan-eligibility-app .

<<COMMENT
# Errors that we encountered in the previous step
# 1. ERROR: invalid tag "Banking-Loan-Eligibility-App": repository name must be lowercase
# 2. failed to create LLB definition: failed to parse stage name "python==3.11.5": invalid reference format. Updated the file with "python:3.11.5"
# 3. executor failed running [/bin/sh -c pip install --no-cache-dir -r requirements.txt]: runc did not terminate sucessfully.
# Uninstalled Docker desktop and docker toolbox. Then re-installed docker desktop and docker toolbox. and it worked
COMMENT

# Trying with Trial and Error
# Update the Dockerfile to create container with latest python
# Build the image using below command
docker build -t banking-loan-eligibility-app .

# Check if there ia any image
# To display the list of images in the repository
docker images


# To create docker container using docker image created in previous step:
docker run -p 5000:5000 banking-loan-eligibility-app:latest


# To remove docker container and docker images
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)

#To run a Docker in interactive mode
docker run -it -p 5000:5000 banking-loan-eligibility-app /bin/bash


# you can copy files or directories from your local system to a Docker container from your local system using - docker cp.
docker cp <source_path> <container_id_or_name>:<destination_path_inside_container>
docker cp requirements.txt 076d92d228f3:/banking-loan-eligibility-app/requirements.txt



# To edit the file in the docker container
apt update
apt install vim