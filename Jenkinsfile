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
                docker {
                    image 'qnib/pytest'
                }

            steps {
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }  
}
