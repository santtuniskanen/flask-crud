pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python app.py'
            }
        }
    }
}