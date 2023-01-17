# simple-server-fun

# Consideration
I will take a TDD approach. 

The most important module to import and use here will be Click(https://click.palletsprojects.com/en/8.1.x/).

It is a simple and sufficient module, ideal for building a command line program quickly.

## Tests
As I am taking a TDD approach, the first set of tests I will write are for the ability to accurately retrieve data from our CPX server. 

I will mock the return values since we should not have to run the server in order to pass our tests. This will shorten the feedback loop and we can dictate the expected values.

