pipeline {
  agent any

  environment {
    COMPOSE_PROJECT_NAME = "jenkins_app"
  }

  stages {
    stage('Build and Deploy') {
      steps {
        sh 'python main.py &'
      }
    }

    stage('Unit tests') {
      steps {
        sh 'pytest'
        }
    }

    stage('Test endpoint') {
      steps {
        sh 'curl -i http://localhost:3000/login'
      }
    }
  }

}
