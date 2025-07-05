pipeline {
  agent any

  stages {
    stage('Setup venv & Install') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Pytest') {
      steps {
        sh './venv/bin/pytest'
      }
    }

    stage('Run App in Background') {
      steps {
        sh '''
          nohup ./venv/bin/python3 main.py > app.log 2>&1 &
          echo $! > app.pid
          sleep 2  
        '''
      }
    }

    stage('Curl App') {
      steps {
        sh '''
          curl -i http://127.0.0.1:8000/
        '''
      }
    }

    stage('Stop App') {
      steps {
        sh '''
          kill $(cat app.pid)
          rm app.pid
        '''
      }
    }
  }
}
