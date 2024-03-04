pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Linting') {
            steps {
                sh 'pylint *.py'
            }
        }
        
        stage('Docker Build') {
            steps {
                sh 'docker build -t salamanteri/flask-crud:latest .'
            }
        }
    }
}