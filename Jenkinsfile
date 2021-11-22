pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Build'
            }
        }
        stage("test PythonEnv") {
                withPythonEnv('python3') {
                    sh 'pip install pytest'
                    sh 'pytest mytest.py'
                }
            }           
        }
    }
}
