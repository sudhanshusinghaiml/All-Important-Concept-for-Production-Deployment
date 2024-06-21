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
- We can create the mongodb-secret.yaml for storing the username and password in the base64 format.
- `echo -n 'password' | base64` - To get the password encoded in base64 format.
- `echo -n 'username' | base64` - To get the username encoded in base64 format.
- Once the mongodb-secret.yaml file is ready. We can apply it using kubectl.
- `kubectl apply -f mongodb-secret.yaml`
- Verify to check if the secret has been created or not - `kubectl get secret`.
- Then this secret file can be referenced into mongodb-deployment.yaml file.
- Sample secret file
    ```YAML
    apiVersion: v1
    kind: Secret
    metadata:
      name: mongodb-secret
    type: Opaque
    data:
      mongodb-root-username: dXNlcm5hbWU=
      mongodb-root-password: cGFzc3dvcmQ=
    ```

## How to use configmap when in the deployment files
- Simlar to secret file, we can create the mongodb-configmp.yaml for storing the DB URL in the configmap.
- Once the mongodb-configmap.yaml file is ready. We can apply it using kubectl.
- `kubectl apply -f mongodb-configmap.yaml`
- Verify to check if the secret has been created or not - `kubectl get configmap`.
- Then this configmap file can be referenced into mongodb-deployment.yaml file.
- Sample Secret file
    ```YAML
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: mongodb-configmap
    data:
      database_url: mongodb-service
    ```


## How to create Internal Service for Database Connection ?
- We are creating Internal service along with the mongo database pod.
- We can also see how secret and config data is used in the ennvironment variables inside the deployment file.
- Image that is used for containerization will openup port - 27017.
- So, we have used the same port for pod and containers for simplicity
- Sample YAML file:
    ```YAML
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: mongodb-deployment
      labels:
        app: mongodb-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: mongodb-app
      template:
        metadata:
          labels:
            app: mongodb-app
        spec:
          containers:
          - name: mongodb-app
            image: mongo
            ports:
            - containerPort: 27017
            env:
            - name: MONGO_INITDB_ROOT_USERNAME
              valueFrom:
                secretKeyRef:
                  name: mongodb-secret
                  key: mongodb-root-username
            - name: MONGO_INITDB_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mongodb-secret
                  key: mongodb-root-password
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: mongodb-service
    spec:
      selector:
        app: mongodb-app
      ports:
        - protocol: TCP
          port: 27017
          targetPort: 27017
    ```


## How to create External Service (also known as Load Balancer) for Database Connection ?
- We are creating External service along with the mongo express application pod.
- We can also see how secret and config data is used in the ennvironment variables inside the deployment file.
- mongo express image that is used for containerization will openup port - 8081.
- So, we have used the same port for pod and containers for simplicity in external service.
- Sample YAML file:
    ```YAML
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: mongodb-express-deployment
      labels:
        app: mongodb-express-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: mongodb-express-app
      template:
        metadata:
          labels:
            app: mongodb-express-app
        spec:
          containers:
          - name: mongodb-express-app
            image: mongo-express
            ports:
            - containerPort: 8081
            env:
            - name: ME_CONFIG_MONGODB_ADMINUSERNAME
              valueFrom:
                secretKeyRef:
                  key: mongodb-root-username
                  name: mongodb-secret
            - name: ME_CONFIG_MONGODB_ADMINPASSWORD
              valueFrom:
                secretKeyRef:
                  key: mongodb-root-password
                  name: mongodb-secret
            - name: ME_CONFIG_MONGODB_SERVER
              valueFrom:
                configMapKeyRef:
                  key: database_url
                  name: mongodb-configmap
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: mongodb-express-service
    spec:
      selector:
        app: mongodb-express-app
      type: LoadBalancer
      ports:
        - protocol: TCP
          port: 8081
          targetPort: 8081
          nodePort: 30000
    ```

## How to execute the deployment manifests ?
- We can execute these manifest using below commands in the order.

    ```sh
    kubectl apply -f mongodb-secret.yaml
    ```

    ```sh
    kubectl apply -f mongodb-configmap.yaml
    ```

    ```sh
    kubectl apply -f mongodb-deployment.yaml
    ```

    ```sh
    kubectl apply -f mongodb-express-deployment.yaml
    ```

- We can check the the status list of all components using below commands

    ```sh
    kubectl get all
    ```

    ```sh
    kubectl get secrets
    ```

    ```sh
    kubectl get configmap
    ```

    ```sh
    kubectl get deployments
    ```

    ```sh
    kubectl get services
    ```

    ```sh
    kubectl get pods
    ```

    ```sh
    kubectl get pods -o wide
    ```

    ```sh
    kubectl get nodes
    ```

- We can check the logs of the pod, service endpoint and its status

    ```sh
    kubectl logs <pod_name>
    ```

    ```sh
    kubectl describe pods <pod_name>
    ```

    ```sh
    kubectl get endpoints <service_name>
    ```

    ```sh
    kubectl get svc <service_name>
    ```

- We execute the below command to run and open service in web browser
    ```sh
    minikube service mongodb-express-service
    ```

- we can save the status of all the deployments using the below commands

    ```sh
    kubectl get deployments mongodb-deployment -o yaml > status/mongodb-deployment-status.yaml
    ```

    ```sh
    kubectl get deployments mongodb-express-deployment -o yaml > status/mongodb-express-deployment-status.yaml
    ```

    ```sh
    kubectl get service mongodb-service -o yaml > status/mongodb-service-status.yaml
    ```

    ```sh
     kubectl get service mongodb-express-service -o yaml > mongodb-express-service-status.yaml
    ```


- We can delete these manifest using below commands in the order.

    ```sh
    kubectl delete -f mongodb-express-deployment.yaml
    ```

    ```sh
    kubectl delete -f mongodb-deployment.yaml
    ```

    ```sh
    kubectl delete -f mongodb-secret.yaml
    ```

    ```sh
    kubectl delete -f mongodb-configmap.yaml
    ```