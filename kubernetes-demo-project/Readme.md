# Steps to Create Kubernetes Deployment file

## Overview of Kubernetes Components
- 2 deployments/pods
- 2 service
- 1 configmap
- 1 secret


## Brief Details about each component and why we need those component?
- **MongoDB Pod** - This component is the pod for MongoDB cluster
- **Internal Service** - This component is the internal service needed to connect the application to Database.
- **Secrets** - This component is needed to store the DB username and password in the base64 encoded format.
- **ConfigMap** - This component is needed to store configuration details such as Mongo DB URL.
- **Deployment** - The deployment components creates the MongoExpress Pods. It uses the ConfigMap and Secrets in the environment variables for the application.
- **MongoExpress Pod** - This component will have the details about MongoExpress Application, DB Connection detials for authetication and External Service.
- **External Service** - This component is to transfer/route the request from Webpage/Application to MongoExpress. And MongoExpress is used to connect to Database for any authentication or data query. In the Kubernetes, we use it with type name `Load Balancer`.


## How to encode secrets when using in the K8s deployment files
- We create the mongodb-secret.yaml for storing the username and password in the base64 format.
- `echo -n 'password' | base64` - To get the password encoded in base64 format.
- `echo -n 'username' | base64` - To get the username encoded in base64 format.
- Once the mongodb-secret.yaml file is ready. We can apply it using kubectl.
- `kubectl apply -f mongodb-secret.yaml`
- Verify to check if the secret has been created or not - `kubectl get secret`.
- Then this secret file can be referenced into mongodb-deployment.yaml file.

