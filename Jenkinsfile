// comments in a Jenkins file?

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
            }
        }
        // builds the new container locally
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build("coateds/python-microservice")
                    app.inside {
                        sh 'echo $(curl localhost:8080)'
                    }
                }
            }
        }

        // stop and remove existing container in try/catch for when there is no container to remove
        stage('Run Docker Container') {
            when {
                branch 'master'
            }
            steps {
                script {
                    try {
                        sh '''
                        docker stop python-microservice
                        docker rm python-microservice
                        '''
                    } catch (err) {}
                    sh '''
                    docker run --name python-microservice -p 80:80 -d coateds/python-microservice
                    '''
                }
            }
        }
    }
}