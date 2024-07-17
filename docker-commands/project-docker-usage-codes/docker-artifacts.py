# =======================================================================================================
#                                       Cleaning up Docker Artifacts
#                                   https://depot.dev/blog/docker-clear-cache
# =======================================================================================================

# To get a breakdown of how much disk space is being taken up by various artifacts
docker system df


# To clear the disk space used by stopped containers
docker container prune

docker container prune -f


# To see the ids of unused containers with filters on the status of the container
docker ps --filter status=exited --filter status=dead -s


# To know the size of the unused container,
docker ps --filter status=exited --filter status=dead -q


# To remove unused images from the system. 
docker image prune -f


# To force the removal of images that uses our system, assuming they're unused images.
docker image prune -a -f


# To remove volumes - 
# Volumes are never cleaned up automatically in Docker because they could contain valuable data
# This removes all anonymous volumes not used by any containers.
docker volume prune -f


# When we see that we didn't reclaim any space from previous step, we have volumes that 
# are associated with containers
# To see these volumes
docker volume ls


"""
    We get an output that shows the driver and the volume name. 
    The command docker volume pruneonly removes anonymous volumes. 
    These volumes are not named and don't have a specific source from outside the container. 
    We can use the "docker volume rm -a" command to remove all volumes
"""
docker volume rm -a


# To remove the Docker build cache, we can run "docker buildx prune" command to clear 
# the build cache of the default builder.
docker buildx prune -f


# If we want to remove the build cache for a specific builder, 
# we can use the --builder flag to specify the builder name
docker buildx prune --builder builder-name -f


# While Docker networks don't take up disk space on our machine, 
# they do create network bridges, iptables, and routing table entries. 
# So we can remove unused networks with the docker network prune command to clean these up.
docker network prune -f



# We can remove all unused artifacts Docker has produced by running docker system prune. 
# This will remove all unused containers, images, networks and build cache.
docker system prune -f



# By default, the above command will not remove volumes and only removes dangling Docker images. 
# We can use the --volumes flag to remove volumes as well. We can also add the -a flag again to 
# remove all images not associated with a container
docker system prune --volumes -a -f