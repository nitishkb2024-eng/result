pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Configured for your specific GitHub repository and the default main branch
                git branch: 'main', url: 'https://github.com/nitishkb2024-eng/result.git'
            }
        }

        stage('Build') {
            steps {
                // Changed from 'sh python3' to Windows 'bat python' based on your console logs
                bat 'python result.py'
            }
        }
    }
}
