# simple-server-fun

# Consideration
I will take a TDD approach. 

The most important module to import and use here will be Click(https://click.palletsprojects.com/en/8.1.x/).

It is a simple and sufficient module, ideal for building a command line program quickly.

## Disclaimer
I ran out of time massively. This includes hastily written code and incomplete tests.

I also have not been able to allow customisation of port number on which cpx_server is hosted. This repo assumes it will always be hosted on port 8080. 

So to run this application, please host it on 8080.

`python3 cpx_server.py 8080`

## Installation
Just Makefile at the root directory to install all dependencies + virtual environment. 

Simply do `make install`.

## Tests
As I am taking a TDD approach, the first set of tests I will write are for the ability to accurately retrieve data from our CPX server. 

I will mock the return values since we should not have to run the server in order to pass our tests. This will shorten the feedback loop and we can dictate the expected values.

All the tests can be run by `make test`.

I tried really hard to pass some e2e tests, but there is unknown behaviours around mocking that really bugged me :weary:

## Running the actual application
`python3 src/thoughtcli.py` will act as your commandline tool.
 
I could not get the commandline to work as it is, like 
`cli --command` unfortunately. 

But all 4 tasks described in the instructions can be executed like so:
1. Print running services to stdout (similar to the table below) 
    `python3 src/thoughtcli.py ip-status --ip_input 10.58.1.1-10.58.1.3`

2. Print out average CPU/Memory of services of the same type
    `python3 src/thoughtcli.py average-stats`

3. Flag services which have fewer than 2 healthy instances running 
    `python3 src/thoughtcli.py display-unhealthy-services`

4. Have the ability to track and print CPU/Memory of all instances of a given service over
time (until the command is stopped, e.g. ctrl + c).
    `python3 src/thoughtcli.py ip-status --ip_input all`


