pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Build'
            }
        }
        stage('Run pytest') {
            steps{
            sh 'pytest mytest.py'
             }
        }
    }
}
