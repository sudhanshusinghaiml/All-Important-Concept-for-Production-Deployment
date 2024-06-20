# To start the minikube clusters
minikube start

# To stop the minikube clusters
minikube stop

# To delete the minikube clusters
minikube delete

# To start the minikube clusters with 3 nodes
minikube start --cpus=2 --memory=2000m --disk-size=20000mb --nodes=3


# To check the status of pods & nodes
minikube status

# Sample output of above commands
# minikube
# type: Control Plane
# host: Running
# kubelet: Running
# apiserver: Running
# kubeconfig: Configured

# minikube-m02
# type: Worker
# host: Running
# kubelet: Running
 
# minikube-m03
# type: Worker
# host: Running
# kubelet: Running
