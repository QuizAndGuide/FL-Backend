pipeline {
    agent any
    stages{
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
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'docker-compose run web python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker-compose up -d'
            }
        }
    }
}
