pipeline {
    agent { label 'agent2' }

    environment {
        IMAGE_NAME = "shivanhussain/system-monitoring-dashboard:latest"
        REPORT_DIR = "trivy-reports"
        EMAIL_TO  = "Your-Email-Address"
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main',
                url: 'https://github.com/ShivanHussain/System-Monitoring-dashboard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build --no-cache -t monitor-app .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh '''
                    echo "Running tests inside container..."
                    docker run --rm monitor-app pytest tests/ -v
                '''
            }
        }

        stage('Trivy Scan') {
            steps {
                sh '''
                    mkdir -p ${REPORT_DIR}

                    echo "Running Trivy Scan..."

                    trivy image \
                    --severity HIGH,CRITICAL \
                    --format table \
                    -o ${REPORT_DIR}/trivy-report-${BUILD_NUMBER}.txt \
                    monitor-app
                '''
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag monitor-app $IMAGE_NAME'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker compose down || true
                    docker compose up -d
                '''
            }
        }
    }

    post {

        success {

            emailext(
                subject: "SUCCESS: Jenkins Build ${env.BUILD_NUMBER}",

                body: """
                Build Successful!

                Job Name: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}

                Docker image built successfully.
                Trivy scan completed.

                Console log and Trivy report attached.
                """,

                to: "${env.EMAIL_TO}",

                attachmentsPattern: "trivy-reports/trivy-report-${BUILD_NUMBER}.txt"
            )

            echo "Pipeline succeeded!"
        }

        failure {

            emailext(
                subject: "FAILED: Jenkins Build ${env.BUILD_NUMBER}",

                body: """
                Build Failed!

                Job Name: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}

                Check attached console log and Trivy report.
                """,

                to: "${env.EMAIL_TO}",

                attachmentsPattern: "trivy-reports/trivy-report-${BUILD_NUMBER}.txt"
            )

            echo "Pipeline failed!"
        }
    }
}