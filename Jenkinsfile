pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Build'
            }
        }
        stage("test PythonEnv") {
            steps{
               sh 'python test_calc.py' 
            }
        }
    }           
}


