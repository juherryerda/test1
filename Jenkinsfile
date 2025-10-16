    // Example Jenkinsfile
    pipeline {
        agent any

        stages {
            stage('Checkout') {
                steps {
                    git 'https://github.com/YOUR_GITHUB_USERNAME/flask-app.git' // Replace with your repo
                }
            }
            stage('Build') {
                steps {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
            stage('Test') {
                steps {
                    // Add commands to run your tests here, e.g.,
                    // sh 'pytest'
                }
            }
            stage('Deploy') {
                steps {
                    // Add deployment commands here, e.g.,
                    // sh 'docker build -t my-flask-app .'
                    // sh 'docker run -d -p 5000:5000 my-flask-app'
                }
            }
        }
    }
