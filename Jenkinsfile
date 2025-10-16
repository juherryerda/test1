pipeline {
    agent anystages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/juherryerda/test1', branch: 'master'
            }
        }stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-api .'
            }
        }stage('Run Docker Container') {
            steps {
                sh '''
                docker stop flask-api || true
                docker rm flask-api || true
                docker run -d -p 7002:7002 --name flask-api flask-api
                '''
            }
        }
    }
}
