// comments in a Jenkins file?

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
            }
        }
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
                    }
                    '''
                    docker run --name python-microservice -p 80:80 -d coateds/python-microservice
                    '''
                }
            }
        }
    }
}