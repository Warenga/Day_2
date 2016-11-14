## Andela Bootcamp 12: Home Day 2

### This repo contains all the projects for Andela Bootcamp Day 2. They include:

1. Andelabs
2. HTTP & WEB

## Andelabs
The Andelabs on this repository are:
	-Word count
		- This is a function that accepts a string and returns a dictionary {words in the string : num of occurence}.  
	-Max and min number
		- A function that accepts a list of numbers, calculates the maximum number and the minimum number and returns a list [min_num, max_num].

## HTTP & WEB
A simple command line application that consumes a Public API using a HTTP client library.

### What it does:
It outputs a certain number of cat facts and allows the user to save the facts.

### How it does this:
It posts user input into the endpoint of the http get request. Formats the response and prints out the cat facts. 
It also asks the user if they want to save the facts. If 'Yes' then it creates and writes into a new file called 'catfacts.txt'.

### Public API SPECS:
- API Endpoint: http://catfacts-api.appspot.com/api/
- API Home Page: http://catfacts-api.appspot.com/doc.html
- Scope: Single purpose API
- Architectural Style: REST
- Supported Response Formats: JSON

### How to run it locally
--------------------------------------------
Have python 2.7 or 3 installed in your machine

<strong>Clone this repository</strong>

<strong>Create a virtualenv</strong>

<strong>Pip install --editable .</strong>

<strong>Run your command line</strong>

<strong>Run 'catfacts'</strong>

Enjoy :)


