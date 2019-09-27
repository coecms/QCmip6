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
2. you can assign yourself a test if you have an idea for a test function.

## To contribute a function
Create a new branch for your function and then push it to this repo.
Add a test wherever possible.
When you're ready to merge it to master create a pull request and choose a reviewer.

