# Docker Commands

## Basic Docker Commands

### Building and Running Docker Containers

- Build a Docker image:
  ```sh
  docker build -t us-visa-approval-prediction .
  ```

- Run a Docker container in detached mode:
  ```sh
  docker run -d -p 8080:8080 us-visa-approval-prediction:latest
  ```

- Run a Docker container interactively:
  ```sh
  docker run -it --rm us-visa-approval-prediction:latest
  ```

- Access a running container:
  ```sh
  docker exec -it inspiring_swanson bash
  ```

### Installing Docker on Ubuntu

- Install Docker:
  ```sh
  sudo apt install docker.io
  ```

### Docker Processes

- Find Docker processes:
  ```sh
  ps -ef | grep [d]ocker
  ```

### Managing Docker Images and Containers

- Display all Docker images:
  ```sh
  docker images
  ```

- Remove a Docker image (ensure the container using it is deleted first):
  ```sh
  docker rmi image_id
  ```

- List all Docker containers:
  ```sh
  docker ps -a
  ```

- Remove a container:
  ```sh
  docker rm container_id
  ```

- Start a container:
  ```sh
  docker start nervous_wright
  ```

- Stop a container:
  ```sh
  docker stop nervous_wright
  ```

- Remove containers:
  ```sh
  docker rm nervous_wright quizicle_euclid
  ```

- List all container IDs:
  ```sh
  docker ps -a -q
  ```

- Bulk delete all stopped containers:
  ```sh
  docker rm $(docker ps -a -q)
  ```

## Running Docker and Getting into a Container

- Run a container and print a message:
  ```sh
  docker run --rm busybox:latest /bin/echo "Hello Docker"
  ```

- Run a container interactively:
  ```sh
  docker run -it --rm busybox:latest
  ```

- Run a container in detached mode:
  ```sh
  docker run -d centos tail -f /dev/null
  ```

- Execute a command in a running container:
  ```sh
  docker exec -it container_name shell
  ```

- Pull a Docker image:
  ```sh
  docker pull tomcat:jre8
  ```

- Run a container with port mapping:
  ```sh
  docker run -d -p 80:8080 bankingcustomerchurnprediction
  ```

## Docker Container Statistics

- List the utilization of all containers:
  ```sh
  docker stats --all
  ```

- List resource stats for a specific container:
  ```sh
  docker stats small_http
  ```
