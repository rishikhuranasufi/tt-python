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
                        sh 'scp -i ${privatefile} ./* ubuntu@13.59.155.51:~/'
			sh ' pwd'
			sh ' ls -lart'
			sh 'ssh -i ${privatefile} ubuntu@13.59.155.51 bash build.sh'
		 }
               }
	    }
	 stage ('Run') {
            steps {                
                withCredentials([sshUserPrivateKey(credentialsId: 'python', keyFileVariable: 'privatefile', passphraseVariable: '', usernameVariable: 'username')]) {             
                        sh ' pwd'
			sh ' ls -lart'
			sh 'ssh -i ${privatefile} ubuntu@13.59.155.51 bash start.sh'
		 }
               }
	    }
        }
    }    
