# =======================================================================================================
#                                       Basic Docker Commands
# =======================================================================================================

docker build -t us-visa-approval-prediction .


docker run -d -p 8080:8080 us-visa-approval-prediction:latest  (detached mode)

docker run -it --rm us-visa-approval-prediction:latest

docker exec -it inspiring_swanson bash


# To install docker.io on Ubuntu Server
sudo apt install docker.io


# To find the process that is running 
ps -ef |grep [d]ocker


# To build a docker image
docker build -t banking-churn-prediction-image .


# To display all the images present in the local repository.
docker images


# To remove images - (ERROR – image is beign used by running container). 
# It will not delete the image until container is deleted. So, if we try after deleting the container.
docker rmi image_id


# To display the list of container in the repository
docker ps -a


# To remove the dead container
# rm  is to remove the container. 
# d is the first letter of the container id (not a good practice to follow)
docker rm d



# To start the container
docker start nervous_wright


# To stop the container
docker stop nervous_wright


# Just stopping the container may not helpful. We have to remove the container
docker rm nervous_wright quizicle_euclid


# This will display the container details along with status
docker ps -a


# This will exit the container immediately.
# When we will access it using the public address, the webpage will be down/gone.
docker stop focused_kellar


# Once we start the container again and try refreshing the webpage, we can view the Tomcat home page.
docker start focused_kellar 


# This will list out all the containers id
docker ps -a -q



# This will bulk delete all the containers that are not running. 
# If you want to remove containers that are running then we need to bulk stop the container and 
# then remove it using below commands
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)


#  will list all the images
docker images


# This will list all the image_id of all the images.
docker images -q


#It will delete all the images
docker rmi $(docker images -q)

# =====================================================================================================


"""
    If there is a dead container hanging out, we can see using below commands and then remove the dead container. 
    We can use 1st few characters of container id or complete name to delete the container.
"""

docker ps -a   # To list the containers
docker rm d    # Removes the dead container
# If there are multiple containers with same starting characters, we will receive error
# Error response from daemon: multiple IDs found with provided prefix: b


# ================================================================================================
"""
    Each container is a process and within that Container there is something called processed ONE. 
    Container is a process from OS perspective. 
    When you get-in the container, it must have processed ONE, which is long running. 
    And as long as that process is running the container will be in running state. 
    And when the process is stopped/terminated, then container will stop.
"""

"""
    Since, every container is a process. When we check the process running on the instances, 
    we should see the 3rd process for container and it should have some parent id associated 
    with one of the processes

"""
# =======================================================================================================



# =======================================================================================================
#                                Running a Docker and Getting into a docker
# =======================================================================================================

"""
    busybox:latest - It will search for the image locally, if not found, it will check docker hub and 
                    install the latest version
    --rm:          - Automatically remove the container when it exits 
"""
docker run –rm busybox:latest /bin/echo “Hello Docker”



"""
    1. Create a container from the image.
    2. Make changes in the container by logging into it.
    3. Create another container from the same image.
    4. We will see that changes made in step 2 will not be available in 2nd container.
"""
# it will download the image and open a docker session/terminal 
docker run --it --rm busybox:latest


# -d: detached mode. Container will continue to execute after the command will end.
docker run --d centos tail -f /dev/null


# to get into a running container
docker exec --it [container] [shell]

docker exec --it nervous_wright bash

sudo ls -al /var/lib/docker/aufs/layers


# It will download all the layers necessary to build the tomcat image
docker pull tomcat:jre8


# -p is for port mapping Port “80” is host port and port 8080 is container port
# -d: detached mode. Container will continue to execute after the command will end
docker run -d -p 80:8080 bankingcustomerchurnprediction

# =========================================================================================================
# This will list out the utilization of all the containers
docker stats –all


# How do we know what resources these containers are consuming?
# This will list all the stats/resources about the consumer
docker stats small_http


docker pull python