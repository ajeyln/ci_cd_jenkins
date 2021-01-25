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