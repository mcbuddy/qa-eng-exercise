# Instruction to run test

I successfully change the SQLite3 to MySQL to be more easier to code and test. Before run the test, we need to 
insert data to database test. I provide sql file for easier to run the test. Just type this to the command.
`mysql -u root exercise < exercise.sql` (Notice: I use root user and did not put password on the mysql command)

## I. Test Hardness
The api test build using same library as the flask app and virtualenv. Using Python 2.7 as current version. 
In order to run test just simply type this command to terminal `python api_test.py` or `python api_test.py -i=local`
By default it will be test the localhost and it can be specify to different env if needed. 

## II. Load Test
The load test using Gatling and Scala as its tools. Java JDK 1.8 needed for this load test 
In order to run test just go to `load_test` directory
then type `./bin/gatling.sh` this command will lists all the available load test and asking the user imput
or simply type this command to run first load test `./bin/gatling.sh -s qa_exercise.GetAllUsers`
The result of the test can be view after the load test done by opening the `results` folder, 
it looks something like this `qa-eng-exercise/tests/load_test/results/getallusers-1519623961390/index.html`

## Caveat:
- Have difficulty with Vagrant file on this file. It gave me error about the `hosts` on the provisioning. 
- For deploy and build automatically, I need CI Server (Jenkins is my recommendation) connected with github hooks.

