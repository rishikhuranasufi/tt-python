pipeline {
    agent { label  "agentfarm" }

    stages {
        stage('Delete the Workspace') {
            steps {
                sh 'sudo rm -rf $WORKSPACE/*'
            }
        }
	 stage('Pull Source Code') {
            steps {
		git credentialsId: 'hp', url: 'git@github.com:rishikhuranasufi/tt-python.git'
            }
        }
        stage ('Initialize') {
            steps {
                sh '''
                    sudo apt install python3-pip python3-venv -y
                    pip3 -V                   
                '''
            }
        }

        stage ('Build') {
            steps {
              sh '''
	          ls -lrt
                  python3 -m venv venv
                  source venv/bin/activate
                  sudo python3 -m pip install -r requirements.txt
              '''
            }
	    }
        }
    }    
