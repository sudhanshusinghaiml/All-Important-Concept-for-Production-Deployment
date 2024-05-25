# Jenkins Pipeline Setup 
- We can use github actions workflow to trigger Jenkins Pipeline. We can setup Jenkins server using the details mentioned below.
- Steps for setting up a Jenkins Server
    - Create an EC2 instance that we can use as Jenkins Server
    - Run the below scripts to setup Jenkins by connecting to the EC2 machine (Jenkins Server)
        ```sh
        sudo apt update     # Update Ubuntu Server with latest package

        sudo apt install openjdk-8-jdk -y   # Commands to install Java

        # This is the Debian package repository of Jenkins to automate installation and upgrade.
        # To use this repository, first add the key to your system (for the Weekly Release Line):
        sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

        # Then add a Jenkins apt repository entry:
        echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

        # Update your local package index, then finally install Jenkins:
        sudo apt-get update
        sudo apt-get install fontconfig openjdk-17-jre
        sudo apt-get install jenkins

        ## Start the jenkins server
        sudo systemctl start jenkins

        ## Enable the jenkins server
        sudo systemctl enable jenkins

        ## Check the status of the jenkins server
        sudo systemctl status jenkins

        # Commands to install Docker

        ## Installing Docker
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker $USER
        sudo usermod -aG docker jenkins
        newgrp docker

        ## Installing AWSCLI
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
        sudo apt install zip -y
        unzip awscliv2.zip
        sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
        sudo usermod -a -G docker jenkins
        ```

    - Run `aws configure` command to setup aws cli access on Jenkins server

    - Restart the Jenkins Server and attach the elastic ip so that it remains same thourhout its life cycle

    - Get the IP address of Jenkins server and try to connect to browser. By default Jenkins open on port 8080

    - Get the password for the first time login by running below commands on Jenkins Server
      ```sh
      sudo cat /var/lib/jenkins/secrets/initialAdminPassword
      ```

## Jenkins File for running Jenkins Pipeline
- Jenkins Pipeline can use the stages mentioned in Jenkinsfile
    ```Jenkinsfile
    pipeline {
        agent any

        environment {
    		ECR_REPOSITORY = credentials('ECR_REPOSITORY')
    		AWS_ACCOUNT_ID = credentials('AWS_ACCOUNT_ID')
    		AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
    		AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        }

        stages {
            // stage('Static Code Analysis') {
            //     steps {
            //         echo 'Scanning Python code using static code analysis...'
            //         sh 'flake8 --max-line-length=120 .'
    		// 		echo 'Scanning Python code - Completed'
            //     }
            // }

            stage('Scan for Large Files') {
                steps {
                    echo 'Scanning repository for large files...'
                    sh 'find . -type f -size +50M'
    				echo 'Scanning repository for large files - Completed'
                }
            }

            // stage('Scan for Credentials') {
            //     steps {
            //         echo 'Scanning files for credentials...'
            //         sh 'trufflehog --regex --entropy=True .'
    		// 		echo 'Scanning files for credentials - Completed'
            //     }
            // }

            stage('Login to ECR') {
                steps {
                    echo 'Logging in to Amazon ECR...'
    				script {
    					sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com'
                    }
    				echo 'Logging in to Amazon ECR - Completed'
                }
            }

            stage('Build Docker Image') {
                steps {
                    echo 'Building Docker image...'
                    sh 'docker build -t $ECR_REPOSITORY .'
    				echo 'Building Docker image - Completed'
                }
            }

            stage('Push Docker Image') {
                steps {
                    echo 'Pushing Docker image to ECR...'
                    sh 'docker push $ECR_REPOSITORY'
    				echo 'Pushing Docker image - Completed'
                }
            }

            stage('Continuous Deployment') {
                steps {
                    echo 'Deploying to EC2 instance...'
                    sshagent(['ec2-ssh-key']) {
                        sh "ssh -o StrictHostKeyChecking=no -l ubuntu 3.86.37.143 'cd /home/ubuntu/ && wget https://github.com/sudhanshusinghaiml/CVProject-Chest-Disease-Classification/blob/develop/docker-compose.yaml && export IMAGE_NAME=$ECR_REPOSITORY:latest && aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.  dkr.ecr.us-east-1.amazonaws.com && docker compose up -d '"
                    }
                }
            }
        }

        post {
            success {
                echo 'Pipeline executed successfully!'
            }
            failure {
                echo 'Pipeline execution failed!'
            }
        }
    }
    ```
