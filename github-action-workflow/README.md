
# Deployment File Explanation

Below is an example of a deployment file with CI and CD as jobs, including static code style check, secret scanning, and code scanning.

```yaml
name: Deploy Application Docker Image to EC2 instance

on:
  push:
    branches: [main]

jobs:
  Continuous-Integration:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 truffleHog

      - name: Static Code Analysis
        run: |
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

      - name: Secret Scanning
        run: |
          trufflehog3 --rules trufflehog3/rules/regular_rules.py --entropy=False --lang python --branch main .

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_DEFAULT_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build, tag, and push image to Amazon ECR
        id: build-image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          ECR_REPOSITORY: ${{ secrets.ECR_REPO }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .  
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
          echo "::set-output name=image::$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/init@v1
        with:
          languages: python

      - name: Perform CodeQL Scan
        uses: github/codeql-action/analyze@v1

  Continuous-Deployment:
    needs: Continuous-Integration
    runs-on: self-hosted
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_DEFAULT_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Deploy Docker Image
        run: |
          docker run -d --name myapp -e AWS_ACCESS_KEY_ID="${{ secrets.AWS_ACCESS_KEY_ID }}" -e AWS_SECRET_ACCESS_KEY="${{ secrets.AWS_SECRET_ACCESS_KEY }}" -e AWS_DEFAULT_REGION="${{ secrets.AWS_DEFAULT_REGION }}" -e MONGODB_URL="${{ secrets.MONGODB_URL }}" -p 80:8080 "${{ steps.login-ecr.outputs.registry }}"/"${{ secrets.ECR_REPO }}":${{ github.sha }}

      - name: Health Check
        run: |
          until $(curl --output /dev/null --silent --head --fail http://localhost:80); do
            printf '.'
            sleep 5
          done
          echo "Application is running!"

      - name: Monitoring and Logging Setup
        run: |
          # Placeholder for monitoring and logging setup commands
          echo "Monitoring and logging setup"

      - name: Rollback Strategy
        if: failure()
        run: |
          docker stop myapp
          docker rm myapp
          docker run -d --name myapp             -e AWS_ACCESS_KEY_ID="${{ secrets.AWS_ACCESS_KEY_ID }}"             -e AWS_SECRET_ACCESS_KEY="${{ secrets.AWS_SECRET_ACCESS_KEY }}"             -e AWS_DEFAULT_REGION="${{ secrets.AWS_DEFAULT_REGION }}"             -e MONGODB_URL="${{ secrets.MONGODB_URL }}"             -p 80:8080 "${{ steps.login-ecr.outputs.registry }}"/"${{ secrets.ECR_REPO }}":previous-image-tag
          echo "Rolled back to the previous version"
```

### Explanation

1. **Continuous Integration Job**:
   - **Checkout**: Checks out the code from the repository.
   - **Set up Python**: Sets up Python 3.8 for the environment.
   - **Install dependencies**: Installs necessary dependencies like `flake8` for static code analysis and `truffleHog` for secret scanning.
   - **Static Code Analysis**: Runs `flake8` to check for code quality issues.
   - **Secret Scanning**: Runs `truffleHog` to scan for secrets in the codebase.
   - **Configure AWS credentials**: Configures AWS credentials using secrets stored in GitHub.
   - **Login to Amazon ECR**: Logs into Amazon Elastic Container Registry (ECR).
   - **Build, tag, and push image to Amazon ECR**: Builds the Docker image, tags it, and pushes it to ECR.
   - **Perform CodeQL Analysis**: Initializes CodeQL for code scanning.
   - **Perform CodeQL Scan**: Analyzes the codebase using CodeQL for vulnerabilities and issues.

2. **Continuous Deployment Job**:
   - **needs: Continuous-Integration**: Indicates that this job depends on the successful completion of the CI job.
   - **Checkout**: Checks out the code from the repository.
   - **Configure AWS credentials**: Configures AWS credentials using secrets stored in GitHub.
   - **Login to Amazon ECR**: Logs into Amazon ECR.
   - **Deploy Docker Image**: Runs the Docker image on an EC2 instance.
   - **Health Check**: Performs a health check to ensure the application is running correctly.
   - **Monitoring and Logging Setup**: Placeholder for setting up monitoring and logging.
   - **Rollback Strategy**: If the deployment fails, stops the current container, removes it, and runs the previous version of the Docker image.
  
## References:
   - For more details about github actions please find follow the attached given url below.
       - [Github Actions](https://github.com/actions)
       - [AWS Github Actions](https://github.com/aws-actions)
       - [Google Github Actions](https://github.com/google-github-actions)
       - [Github Actions for Azure](https://learn.microsoft.com/en-us/azure/developer/github/github-actions)
