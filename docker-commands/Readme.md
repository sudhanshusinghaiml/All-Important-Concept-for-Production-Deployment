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

- Check logs of the conatiner:
  ```sh
  docker logs inspiring_swanson
  ```
  
- Check streaming logs of the conatiner:
  ```sh
  docker logs -f inspiring_swanson
  ```
  
- View Logs from a Specific Timestamp
  ```sh
  docker logs -f --since="2023-01-01T00:00:00" <container_id_or_name>
  ```

- Run a Docker container interactively:
  ```sh
  docker run -it --rm us-visa-approval-prediction:latest
  ```
  
- Run a Docker container interactively on specific port:
  ```sh
  docker run -it --rm -p 8080:8080 inspiring_swanson
  ```

- Access a running container:
  ```sh
  docker exec -it inspiring_swanson bash
  ```
  
###  Clean up Docker system

- Cleaning up system spaces
  ```sh
  docker system prune -f
  ```

- List all volumes to ensure no volumes are dangling:
  ```sh
  docker volume ls
  docker volume prune -f
  ```

- Cleaning up image spaces
  ```sh
  docker image prune -f
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
  
  ```sh
  docker rm -f container_id
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
  
  ```sh
  docker run -it --rm -p 8080:8080 busybox:latest
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
