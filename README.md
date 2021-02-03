<h1 align="center">JENKINS AGENDA</h1>

Jenkins install locally :

https://www.lambdatest.com/blog/jenkins-pipeline-tutorial/

1. INSTALLATION : https://www.youtube.com/watch?v=3Ax9bcj3OrM

2. TEST SECTION:  https://www.youtube.com/watch?v=_o42ZCkCJb4

3. GITHUB PUSH TRIGGER: https://www.youtube.com/watch?v=Z3S2gMBUkBo

Primer 
Install:
* installation, initial password
* setup user and password (not to mess here)
* give valid email address

Workiing:
* code snippet generator
* server setup 
* Plugins, manage
* create new item, pipeline

Jenkinsfile
* direct scripting on portal
* jenkinsfile (why?)

End-to-end running
* Stage : checkout (Github creds)
* Stage : python envt setup
* Stage:  Execute linting
* Stage : Execute unittesting
* Stage:  execu9te main ( Please take command line args from user)
* Stage: Finish
	* deactivate python envt
	* archive artifacts
		* lint.txt
		* pytest.txt
		* logging.log
	* clean workspace#

Jenkins authentication
------------------------
1. under "Manage Jenkins" create Jenkins credentials for Github with username and password.
   This credential gets unique Credential ID. you can use this credential ID for all git tasks in authentcation

2. For git checkout tasks, use the pipeline script generator for generating the code. This code uses your credential id..
it never shows username or password.. CredentialID given by your jenkins is different than jenkins used by others.. that is why it is safe.
So if someone uses this jenkins file on his jenkins, he cannot do git clone as his jenkins does not know this credential id.
   checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a136ccca-41fb-409a-85aa-e214da643754', url: 'https://github.com/vazudew/ALWAYS-PLAN.git']]])
   

Jenkinsfile Setup
------------------------
1. Discarding builds after 10 tasks, groovy code
properties([[$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10']]]);

2. parameterization
more information: https://st-g.de/2016/12/parametrized-jenkins-pipelines
see this pattern, you can keep adding more values, in the parameters list
properties([
  parameters([
    string(name: 'DEPLOY_ENV', defaultValue: 'TESTING', description: 'The target environment', )
   ])
])

3. Approval stage code
stage('Continue approval'){
    input "Do you want to continue to next stage?"
}

4. Change directory
When you clone for the first.. a folder with name of repository gets created in workspace.
For example git cone https://github.com/vazudew/ci-cd-jenkins will create ci-cd-jenkins folder
So you must change to this root directory for all your operations

stage("Linting"){
dir('ci-cd-jenkins') {
      bat 'pylint source'
    }
}
stage("main"){
dir('ci-cd-jenkins') {
      bat 'python source/main.py "Ajey Nayak" 13 278 '
    }
}

6. archiving all the files and copy
read this link carefully : https://medium.com/@gustavo.guss/jenkins-archive-artifact-save-file-in-pipeline-ac6d8b569c2c
and learn by trial and error method