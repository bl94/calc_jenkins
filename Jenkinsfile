pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Jenkins minimum pipeline'
      }
    }
      stage('Test') {
            agent any
              steps {
                  sh 'python test_calc.py'
            }
        }
    }  
}
