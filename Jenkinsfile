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
    
        stage ('Build') {
            steps {                
                withCredentials([sshUserPrivateKey(credentialsId: 'python', keyFileVariable: 'privatefile', passphraseVariable: '', usernameVariable: 'username')]) {             
                        sh 'scp -i ${privatefile} ./* ubuntu@3.12.104.242:~/'
			sh ' pwd'
			sh ' ls -lart'
			sh 'ssh -i ${privatefile} ubuntu@3.12.104.242 bash build.sh'
		 }
               }
	    }
	 stage ('Run') {
            steps {                
                withCredentials([sshUserPrivateKey(credentialsId: 'python', keyFileVariable: 'privatefile', passphraseVariable: '', usernameVariable: 'username')]) {             
                        sh 'ssh -i ${privatefile} ubuntu@3.12.104.242 bash start.sh'
			sh ' pwd'
			sh ' ls -lart'
		 }
               }
	    }
        }
    }    
