# Basic Kubectl Commands
kubectl version

#Metrics
# The kubectl top command returns current CPU and memory usage for a cluster’s pods or nodes, or for a particular pod or node if specified.
kubectl top

# Lists all the components that are running in K8s Cluster
kubectl get all

# List all kubernetes components
kubectl get pods -n kube-system

# Lists all the nodes that is running on Kubernetes
kubectl get nodes

# To create a deployment using app name and image name
# This command will download the image nginx from docker hub
kubectl create deployment nginx-app --image=nginx

# To fetch all the active deployments
kubectl get deployment

# To fetch the active pods where the deployment is running
kubectl get pods

# To fetch the active pods where the deployment is running
kubectl get replicaset


# To edit the deployment of an application that is running
kubectl edit deployment nginx-app

# If we update the replicaset to 3 in the deployment file and save the file
# The deployment changes will be automatically applied.
# We can verify it by running below commands
kubectl get deployment
kubectl get pods
kubectl get replicaset

#===========================================================#
#				Debugging pods								#
#===========================================================#
# To show read the details in the log file for idnetifying any error or issues
kubectl logs <pod_name>

# Creating an App with Mongo DB to validate the logs
kubectl create deployment mongo-app --image=mongo

# Check if the pods started running or not
kubectl get pod

#if the pod is not running, use the describe command 
# to verify the status change of the pod
kubectl describe pod <pod_name>

# To check for errors or Invalid message for debugging the issue
kubectl logs <pod_name>

# To open the interactive terminal of mongo app container 
kubectl exec -it <pod_name> -- /bin/bash

#===========================================================#
#				Delete Deployments							#
#===========================================================#
kubectl get deployment

kubectl get pods

kubectl get replicaset

# To delete the deployment and other layers - pods, replicaset etc
kubectl delete deployment <deployment_name>

#===========================================================#
#			Applying Kubernetes Configuration Files			#
#===========================================================#
# When creating deployment, we have choices to provide multiple options.
# But it is not always that we remember and use all the options correctly.
# Therefore, to avoid erroneous deployment we can create config file and 
# deploy those configurations by applying changes from the config-file

kubectl apply -f <file_name>

# This will create deployment, pods and replicaset as mentioned in the config file
kubectl apply -f nginx-deployment.yaml

# Verify the pods by running below set of commands
kubectl get deployment
kubectl get pods
kubectl get replicaset

# If we want to update/change the configuration file, 
# we can edit the configuration files and apply the changes again
# kubernetes knows when to create or update the deployment
kubectl apply -f nginx-deployment.yaml

#===========================================================#
# Applying Deployment and Service Configuration Files		#
#===========================================================#

# To create deployment, pods and containers based on deployment configuration
# All the resources are labeled with same name.
# For example, metadata labels and tempelate labels are same 
# and is validated with spec matchlabels condition 
kubectl apply -f nginx-deployment.yaml

# Similarly selector in spec makes mkes connection with deployment
# and pods in terms of labels that is used - app: nginx
kubectl apply -f nginx-service.yaml

# Running below commands shows that service is open on port 80
kubectl get service

# How to validate if service is pointing to right pods ?
# How to validate if service forwards request to right port number?
kubectl describe service nginx-service

## Name:              nginx-service
## Namespace:         default
## Labels:            <none>
## Annotations:       <none>
## Selector:          app=nginx
## Type:              ClusterIP
## IP Family Policy:  SingleStack
## IP Families:       IPv4
## IP:                10.97.8.228
## IPs:               10.97.8.228
## Port:              <unset>  80/TCP
## TargetPort:        8080/TCP
## Endpoints:         10.244.1.3:8080,10.244.2.4:8080
## Session Affinity:  None
## Events:            <none>

# IP Address showing in endpoints should point to the correct pods.
# We can verify that by checking pods details
kubectl get pods -o wide

# minikube       Ready    control-plane   5h41m   v1.30.0   192.168.49.2   <none>        Ubuntu 22.04.4 L
# minikube-m02   Ready    <none>          5h40m   v1.30.0   192.168.49.3   <none>        Ubuntu 22.04.4 L
# minikube-m03   Ready    <none>          5h40m   v1.30.0   192.168.49.4   <none>        Ubuntu 22.04.4 L

# How to validate whether status is automaticaly generated or not?
kubectl get deployment nginx-deployment -o yaml

# Saving the current status in file for reference
kubectl get deployment nginx-deployment -o yaml > nginx-deployment-status.yaml

# To delete all the nodes and cluster for this project
kubectl delete -f nginx-deployment.yaml
kubectl delete -f nginx-service.yaml
