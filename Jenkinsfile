pipeline {
    agent any

    environment {
        IMAGE_NAME = "30301207/imt2023035-todo"
        DOCKERHUB = credentials('dockerhub-creds')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker image') {
            when { expression { currentBuild.currentResult == "SUCCESS" } }
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Push Docker image') {
            when { expression { currentBuild.currentResult == "SUCCESS" } }
            steps {
                bat "docker login -u %DOCKERHUB_USR% -p %DOCKERHUB_PSW%"
                bat "docker push %IMAGE_NAME%"
            }
        }
    }
}
