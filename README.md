# QCmip6
This repository aim is to produce qc tests for CMIP6 data.
The initial plan is to create a list of CMIP6 issues we want to identify and create a test for each of them,
These tests will be run intially on a subset of frequently used variables/experiments.
The results will be added to the sqlite clef.db used by the CMIP6 query tool CleF.
In this way a warning can be returned to a user when querying data via CleF if an issue is found for one of the returned simulations.
The db implentation might be separate from this repo, at least initially.
Eventually we'll need to create a framework to run the tests and save the results in the db.
At this stage we're focusing on listing issues and creating the actual test as separate functions.

## How to contribute
There are two ways you can contribute:
1. you can open an issue to propose a test or to signal an issue you have found.
2. you can assign yourself a test if you have an idea for a test function.In regard to that I’m not fully clear about how to use the issues.

## To add issue
At the moment I image 3 kind of issues:
1) Actual bugs with whatever code we produce 
2) an issue with CMIP6 we want to signal, so the problem and potentially an example that we can use to test whatever function we might generate
3) a qc-issue I.e. Something describing a proposed test and following its evolution indicated by a "qc" label (or maybe we could use enhancement?)
While obviously the second kind of issue can and probably will evolve in the third, I would like to apply the qc label only once a test has been proposed and agreed on,
 to make it clear for anyone who wants to contribute a function that is something they can start working on

## To contribute a function
Create a new branch for your function and then push it to this repo.
Add a test wherever possible.
When you're ready to merge it to master create a pull request and choose a reviewer.
