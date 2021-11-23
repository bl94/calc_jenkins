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
                  sh 'nosetests test_calc.py'
            }
        }
    }  
}
