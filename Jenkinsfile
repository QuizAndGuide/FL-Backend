pipeline {
    agent {
        label 'kcrams server'
    }
    stages {
        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                    def result = sh(script: 'python3 manage.py test', returnStatus: true)
                    if (result != 0) {
                        error "Test failed. Stopping the pipeline."
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Obtener información del usuario
                    def userId = env.BUILD_USER_ID
                    def username = env.BUILD_USER

                    echo "Ejecutando la construcción como el usuario: ${username} (ID: ${userId})"
                    
                    // Resto de tus pasos de construcción aquí
                    sh 'docker-compose build'
                }
            }
        }

        // stage('Run Tests') {
        //     steps {
        //         script {
        //             echo 'Running tests...'
        //             def result = sh(script: 'docker-compose run web python manage.py test', returnStatus: true)
        //             if (result != 0) {
        //                 error "Test failed. Stopping the pipeline."
        //             }
        //         }
        //     }
        // }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker-compose up -d'
            }
        }
    }
}
