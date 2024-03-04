pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Linting') {
            steps {
                catchError(buildResult: 'SUCCESS') {
                    sh 'pylint *.py'
                }
            }
        }
        
        stage('Run Flask app') {
            steps {
                sh 'python3 app.py &'
                sleep 10
            }
        }

        stage('Stop Flask app') {
            steps {
                script {
                    sh 'pkill -f "python3 app.py"'
                }
            }
        }
    }
}