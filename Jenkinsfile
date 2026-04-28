pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        IMAGE_NAME = "shivanhussain/system-monitoring-dashboard:latest"
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/ShivanHussain/System-Monitoring-dashboard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t monitor-app .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh '''
                    echo "Running tests inside container..."

                    docker run --rm monitor-app pytest -v
                '''
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag monitor-app $IMAGE_NAME'
            }
        }

        stage('Docker Login & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerHub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker-compose down || true
                    docker-compose up -d
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}