pipeline {
    agent any

    environment {
        // Define your Docker Hub registry settings
        DOCKER_HUB_USER = 'your_dockerhub_username'
        IMAGE_NAME      = 'shopping-calc'
        
        // Dynamically create a unique tag using the Git Commit SHA for strict version tracking
        IMAGE_TAG       = "${env.GIT_COMMIT ? env.GIT_COMMIT.take(7) : 'v1'}"
        
        // Credential IDs configured in your Jenkins credentials store
        DOCKER_CREDS_ID = 'docker-hub-credentials'
        KUBE_CREDS_ID   = 'kubernetes-config-credential'
    }

    stages {
        stage('(1) Source Code') {
            steps {
                // Checkout code automatically handled if running from a Multibranch pipeline,
                // otherwise explicitly checked out here:
                checkout scm
            }
        }

        stage('(2) Continuous Integration') {
            steps {
                echo 'Running automated test suites...'
                // Sets up virtual environment, installs requirements, and runs pytest
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('(3) Build') {
            steps {
                echo "Building Docker image: ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                
                // Build the image locally on the Jenkins agent
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                
                // Securely log into Docker Hub and push the uniquely tagged image
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDS_ID}", usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('(4) & (5) Deployment & Service') {
            steps {
                echo "Updating manifests and deploying to Kubernetes..."
                
                // Securely extract the Kubeconfig file and use it to deploy to your cluster
                withCredentials([file(credentialsId: "${KUBE_CREDS_ID}", variable: 'KUBECONFIG')]) {
                    sh """
                        # Dynamically substitute placeholder strings with the environment configuration
                        sed -i 's|DOCKERHUB_USERNAME|'${DOCKER_HUB_USER}'|g' deployment.yaml
                        sed -i 's|IMAGE_TAG|'${IMAGE_TAG}'|g' deployment.yaml
                        
                        # Apply configuration manifests directly to the cluster
                        kubectl --kubeconfig=${KUBECONFIG} apply -f deployment.yaml
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up build workspace environment...'
            // Remove local docker images to save runner space
            sh "docker rmi ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
    }
}