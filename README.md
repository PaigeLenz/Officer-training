### Installing Python
### Learning Markdown
### JSON Requests
### Input Validation
### Postman Calls
### Object Orientation
### YAML Files
### Hashing Algorithms
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
