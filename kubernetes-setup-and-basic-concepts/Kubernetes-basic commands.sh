# What is a Kubernetes cluster?
# What are the different parts of the Kubernetes architecture?
# What exactly do you mean by "container orchestration"?
# What are the various features of Kubernetes?
# Explain the relationship between Kubernetes and Docker?

# Command to seek help
kubectl get --help

# List all pods in ps output format
kubectl get pods

# List all pods in ps output format with more information (such as node name)
kubectl get pods -o wide

# To describe the pod that is running the image
kubectl describe pod hello

# List a single replication controller with specified NAME in ps output format
kubectl get replicationcontroller web

# List deployments in JSON output format, in the "v1" version of the "apps" API group
kubectl get deployments.v1.apps -o json

# List a single pod in JSON output format
kubectl get -o json pod web-pod-13je7

# List a pod identified by type and name specified in "pod.yaml" in JSON output format
kubectl get -f pod.yaml -o json

# List resources from a directory with kustomization.yaml - e.g. dir/kustomization.yaml
kubectl get -k dir/

# Return only the phase value of the specified pod
kubectl get -o template pod/web-pod-13je7 --template={{.status.phase}}

# List resource information in custom columns
kubectl get pod test-pod -o custom-columns=CONTAINER:.spec.containers[0].name,IMAGE:.spec.containers[0].image

# List all replication controllers and services together in ps output format
kubectl get rc,services

# List one or more resources by their type and names
kubectl get rc/web service/frontend pods/web-pod-13je7

# List the 'status' subresource for a single pod
kubectl get pod web-pod-13je7 --subresource status

