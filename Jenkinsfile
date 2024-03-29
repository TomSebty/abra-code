pipeline {
    agent any 

    stages {
        stage('Code Format') {
            steps {
                script {
			def format = sh (script: 'python3 -m pycodestyle project/web_service.py', returnStdout: true)
			println "${format}"
                        if (!format == ""){
                                currentBuild.result = 'ABORTED'
                                error('Code format is faulty. Please fix the following issues: ${format}')
                        }
		    }
		}
            }
        stage('Linting') {
            steps {
                echo 'Linting...'
		script {
                        def lint = sh (script: 'python3 -m pylint project/web_service.py', returnStdout: true)
                        println "${lint}"
                        if (!lint == ""){
                                currentBuild.result = 'ABORTED'
                                error('Linting failed. Please fix the following issues: ${lint}')
                        }
                    }
                }
            }
	//stage('Unit Testing'){
        //    steps{
        //        script{
        //            sPid = sh (script: 'flask --app project/web_service.py run -h 0.0.0.0 -p 5000 & echo \$!', returnStdout: true).toString().trim()
	//	    def test= sh (script: 'python3 project/tests/web-service_tests.py', returnStdout: true).toString().trim()
        //            println "${test}"
	//	    sh 'kill -9 ${sPid}'
        //            if (!test.contains("All good")){
        //                    currentBuild.result = 'ABORTED'
        //                    error('The unit tests have failed. Please fix any issues and try again. ${test}')
        //            }
        //        }
        //    }
        //}
	stage('Build docker image'){
            steps{
                script{
                    sh 'docker stop web-service || true && docker rm web-service || true' // Stop and remove container if running
                    sh 'docker image prune' // Remove the previously built image
                    sh 'docker build -t tom-web-service:1.0 -t tom-web-service:latest -f project/Dockerfile ./project/' // Build the new version. Need to use commit ID for tagging
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
		script{
                    //sh 'docker run -p 5000:5000 --name web-service -d tom-web-service:latest'
		    docker.image('tom-web-service:latest').withRun('-p 5000:5000 --name web-service') {
		        def test= sh (script: 'python3 project/tests/web-service_tests.py', returnStdout: true).toString().trim()
		        println "${test}"
		        if (!test.contains("All good")){
		            currentBuild.result = 'ABORTED'
		       	    error('The unit tests have failed. Please fix any issues and try again. ${test}')
			}
		    }
		    sh 'docker ps -a'
                }
            }
        }
        stage('Testing') {
            steps {
                echo 'Testing...'
		script {
		    try {
		        def test= sh (script: 'python3 project/tests/web-service_tests.py', returnStdout: true).toString().trim()
		        println "${test}"
		        if (!test.contains("All good")){
		            currentBuild.result = 'ABORTED'
		       	    error('The unit tests have failed. Please fix any issues and try again. ${test}')
			}
		    }
        	    finally {
		        sh 'docker stop web-service || true && docker rm web-service || true'
	            }
		}
            }
        }
    }
}
