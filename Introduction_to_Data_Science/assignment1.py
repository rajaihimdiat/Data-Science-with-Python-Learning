
# # Assignment 1
"""
For this assignment you are welcomed to use other regex resources such a regex "cheat sheets" you find on the web.
Before start working on the problems, here is a small example to help you understand how to write your own answers. In short, the solution should be written within the function body given, and the final result should be returned. Then the autograder will try to call the function and validate your returned result accordingly. 
"""
def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"
    result = example_string.split(" ")
    return len(result)


# ## Part A

import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    pattern = "[A-Z][a-z]*"
    return re.findall(pattern, simple_string)

assert len(names()) == 4, "There are four names in the simple_string"

"""
## Part B
The dataset file in [assets/grades.txt](assets/grades.txt) contains a line separated list of people with their grade in 
a class. Create a regex to generate a list of just those students who received a B in the course.
"""
import re
def grades():
    with open ("./Assignemnt#1/grades.txt", "r") as file:
        grades = file.read()
    pattern = "[\w]*\ [\w]*(?=:\ B)"
    return re.findall(pattern, grades)

assert len(grades()) == 16


# ## Part C
"""
Consider the standard web log file in [assets/logdata.txt](assets/logdata.txt). This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
* a host (e.g., '146.204.224.152') 
* a user_name (e.g., 'feest6811' **note: sometimes the user name is missing! In this case, use '-' as the value for the username.**)
* the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
* the post request type (e.g., 'POST /incentivize HTTP/1.1' **note: not everything is a POST!**)

Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
```
example_dict = {"host":"146.204.224.152", 
                "user_name":"feest6811", 
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"}
"""
import re
def logs():
    with open("./Assignemnt#1/logdata.txt", "r") as file:
        logdata = file.read()
        pattern = """
                    (?P<host>[\d]*.[\d]*.[\d]*.[\d]*)    
                    (\ -\ )  
                    (?P<user_name>[\w-]*) 
                    (\ \[) 
                    (?P<time>\w*/\w*/.*)
                    (\]\ \") 
                    (?P<request>.*)
                    (")
                    """
    result = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())
    
    return result

assert len(logs()) == 979

one_item={'host': '146.204.224.152',
            'user_name': 'feest6811',
            'time': '21/Jun/2019:15:45:24 -0700',
            'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"


print('The word count is : ',example_word_count())
print('The name of stduents who graded are: ',grades())
print('The first name of stduents: ',names())
print('The logs are (Samples for the first five): ',logs()[0:5])