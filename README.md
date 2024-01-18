### Installing Python
Install vscode from their website and python from their website. Then, through vscode, install the python extension. Now that everything has been installed, you are able to start coding in Python!
### Learning Markdown
Imported beautifulsoup to create a webscraper. You will need to let the code know the website you want searched. Then clarify what it is that you want the code to find. Then clarify how you want the code to print out the information.
### JSON Requests
For this code you will need to install and import flask. Once you import flask, you can create an IP address with an open port. Through that you can add information to a blank webpage and by running the code you can enter the ip address, port and extension into the search bar and get the information that you need.
### Input Validation
Writing a code that asks the user for an input and if that input meets the criteria then either continue that action or send a success message. If not send an error message. To do this you need a part of your code that has the criteria that you expect from the user, then ask the user for the input and have the code decide if it meets the criteria. 
### Object Orientation
For this code, you need to define what list you will create and what variables you want to define with each object. Then, create that list and the variables that come along with the list. Then decide what you want to be printed out. 
### YAML Files
For this you will have to create a docker along with the image. For this I have chosen next cloud so I have found an image that I clarified in the code along with what port will be open for that. Then I repeated the same steps for Minecraft as well.
### Hashing Algorithms
For this you will need to create a block and then create a hash so when you create a new block it will hash it.
### DevOps Practices
Since I am just starting I will probably have a lot of issues, my action is to make a script that will show the issue number, the fact that it was me making the mistake, and a little message for them

```
on:
  issues:
    types: [opened]

jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Thank you for reporting!'
            })

```
