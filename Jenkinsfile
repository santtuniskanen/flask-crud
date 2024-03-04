pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python app.py'
            }
        }
    }
}