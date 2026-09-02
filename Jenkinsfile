pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'git remote add origin https://github.com/nitishkb2024-eng/result.git'
            }
        }

        stage('Build') {
            steps {
                bat 'result.py'
            }
        }
    }
}