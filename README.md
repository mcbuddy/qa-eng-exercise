# Quartet Infrastructure Candidate Exercise

This exercise is an opportunity for you to express your skills and knowledge outside the typical interview process. It is intended to take a short amount of time, so please limit yourself to a couple of hours to complete it.

## Exercise

It is our hope that you understand that being an QA Engineer at Quartet is a multifacted role. As such, we have designed this exercise to afford you a broad range of ways to express your talent and/or interest in various tools. Therefore, we do not expect any one solution. Rather, we are more interested in elegant and simple solutions using your favorite tools with an understanding of alternatives and tradeoffs.

Within this folder you will find a few files that are the beginnings of a basic Python web application (it may contain some bugs too). It should be your goal to enrich and test this project.

The main requirements are:

 1. Build a **test harness** that tests each endpoint of the application. Use the language or tool of your choosing.
 2. Write a **load test** script that runs your test harness to simulate load. Use any tool/framework that you like.

Extra credit:

 3. Upgrade the persistence layer to a **MySQL database**
 4. Configure the application to **switch between persistence backends** via a passed-in (or environment) variable
 5. Write a script that runs a load test for each backend and **compares performance characteristics**

You may find that it is helpful to extend the application in other ways, but this is not required. Some of those extensions may include:

* Use `virtualenv`
* Use a Vagrant provisioner (e.g. Ansible)
* Run an appropriate WSGI server
* Configure a reverse proxy
* Collect metrics
* Introduce Docker

Please remember that this should all be able to be run in an automated fashion. When you have finished the exercise provide us with any instructions to build, run, or deploy the changes you have made to this project in a file named `INSTRUCTIONS.md`.

And finally, please do not spend more time than you feel is appropriate for you. If there are lessons that you have learned, or things you did not have time to do that you would have liked to, simply describe them in an appropriate amount of detail in a file named `NOTES.md`.

When you believe that you have spent a sufficient amount of time on this, package all the files together in a compressed archive format and send it to `talent@quartethealth.com` with the subject line "Infrastructure Engineer Exercise Completed". Good luck!

### Files

The following is a description of the existing files that come packaged with this exercise:

#### Vagrantfile

This is a [Vagrant](https://www.vagrantup.com/) configuration file. It will, by default, spin up two Ubuntu 16.04 ([systemd](https://www.freedesktop.org/wiki/Software/systemd/) based) virtual machines.

#### server.py

This is a basic Python HTTP API built with [Flask](http://flask.pocoo.org/) and a few additional software libraries. It performs some basic work and does some logging as well.

#### requirements.pip

This file contains the depdencies for the Python applications.
