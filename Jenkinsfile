pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        IMAGE_NAME = "vde_django:${BUILD_NUMBER}"
        PYTHONUNBUFFERED = 1
    }

    stages {

        stage('📥 Checkout code') {
            steps {
                echo "🔄 Cloning the repository..."
                checkout scm
            }
        }

        stage('🐍 Setup Python & Install Dependencies') {
            steps {
                echo "⚙️ Creating virtualenv & installing requirements..."
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip list
                '''
            }
        }

        stage('✅ Run Django tests') {
            steps {
                echo "🚀 Running tests..."
                sh '''
                    . ${VENV_DIR}/bin/activate
                    export PYTHONPATH=$PWD
                    python3 manage.py test
                '''
            }
        }

        stage('🐳 Docker build') {
            steps {
                echo "📦 Building Docker image ${IMAGE_NAME}..."
                sh '''
                    docker build -t ${IMAGE_NAME} .
                    docker images | grep vde_django
                '''
            }
        }
  
        // Optionnel : push image vers Docker Hub
        // stage('Push Image') {
        //     steps {
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
        //             sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
        //             sh "docker tag ${IMAGE_TAG} yourdockerhubuser/${APP_NAME}:${BUILD_NUMBER}"
        //             sh "docker push yourdockerhubuser/${APP_NAME}:${BUILD_NUMBER}"
        //         }
        //     }
        // }

        // Optionnel : déploiement SSH, rsync, etc.
  }

    post {
        always {
            echo '🧼 Cleaning up (if needed)...'
        }
        success {
            echo '🎉 CI pipeline completed successfully!'
        }
        failure {
            echo '❌ CI pipeline failed!'
        }
    }
}
