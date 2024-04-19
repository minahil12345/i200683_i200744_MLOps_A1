pipeline {
    agent any
    
    stages {
        stage('Initialize'){
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t flask-app .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh 'docker tag flask-app <your_dockerhub_username>/flask-app'
                    sh 'docker push <your_dockerhub_username>/flask-app'
                }
            }
        }
    }
}
