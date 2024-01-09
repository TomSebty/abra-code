pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
		script {
			def test= sh (script: 'python web-service_tests.py', returnStdout: true).toString().trim()
			println "${test}"
			if (!test.contains("All good")){
				currentBuild.result = 'ABORTED'
	                        error('The unit tests have failed. Please fix any issues and try again.')
			}
		}
            }
        }
    }
}
