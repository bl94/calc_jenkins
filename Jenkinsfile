pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Build'

                }
            }
            stage('Test') {
                steps {
                echo 'Test'
                sh'python -m py_compile test_calc.py'
                stash(name: 'compiled-results', includes: '*.py*')
                }
            }
        }
    }
