    // Example Jenkinsfile
    pipeline {
         agent any // Or specify a specific agent label
    stages {
        stage('Install Python') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip' // Example for Debian/Ubuntu
                // Or for Red Hat/CentOS: sh 'sudo yum install -y python3 python3-pip'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
    }
