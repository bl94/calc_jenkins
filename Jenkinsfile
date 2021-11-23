pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Jenkins minimum pipeline'
      }
    }
    stage('test'){
      steps{
        echo 'Testing'
      }
    }  
  }
}
node
{
   stage('Run pytest') 
   {
       bat "pytest test_calc.py"
   }    
}
