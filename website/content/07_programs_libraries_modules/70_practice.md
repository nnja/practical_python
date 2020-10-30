+++
title = "Practice"
date = 2020-08-29T17:01:32-07:00
weight = 70
+++

## Running Code

Let's create a basic program that we can run as a file on the command line. We'll start with a basic framework using a `main()` function.

```python
# file_execise.py

def main():
    pass

if __name__ == "__main__":
    main()
```

Save your file as `file_exercise.py` and run it from the command line using `python file_exercise.py`.

What happened? Because you ran the file directly, the file's `__name__` variable is set to `__main__`, which triggers the `if` statement to run the `main()` function. This is a common pattern that you'll see in Python programs, and it comes in handy for being able to write programs that work both on their own and when imported into other programs. The `pass` keyword does nothing, it's just there to keep the empty `main()` function from throwing a syntax error.

Let's start filling in our `main()` function. We have a json file named `cities.json` which contains the top five cities in the US, sorted by population. You can [download `cities.json` here](/code/cities.json). Let's open the file and load in the data.

```python
# file_execise.py

import json

def main():
    cities_file = open("cities.json")
    cities_data = json.load(cities_file)
    print(cities_data)

if __name__ == "__main__":
    main()
```

First, we imported the built-in `json` library to help us decode the json file. Then, we opened the file using the `open()` function, and passed the open file handle to the `json.load()` function. The `load()` function read our data in and spit it out as a Python representation - in this case, a list of dictionaries. We then print this list.

```bash
(env) $ python file_execise.py
```

This list is a little hard to make sense of in its raw form, let's print it a little nicer. Use `enumerate()` to go through the list and print it nicely:

```python
# file_execise.py

import json

def main():
    cities_file = open("cities.json")
    cities_data = json.load(cities_file)

    print("Largest cities in the US by population:")

    for index, entry in enumerate(cities_data):
        print(f"{index + 1}: {entry['name']} - {entry['pop']}")

if __name__ == "__main__":
    main()
```

A few new things here: first, remember that `enumerate()` outputs a tuple of (index, entry), so we use `index` and `entry` variables to capture those. Then, for every item in the list, we print the index (+ 1, because zero-indexed lists are sometimes hard to read), and we pull the name and population out of each entry dictionary using the dictionary `[]` syntax.

```bash
(env) $ python file_execise.py
```

One more thing to clean up - using the `open()` keyword on its own is frowned upon, because it won't automatically close any resources you might open. Even if you call the `close()` keyword yourself, there's no guarantee your program won't crash, leaving important resources dangling. It's safer to open files inside a context using the `with` keyword. Once your code exits the scope of the context, your file is automatically closed. Note: our reading and formatting code has shifted to the right because of the change in scope.

```python
# file_execise.py

import json

def main():
    with open("cities.json") as cities_file:
        cities_data = json.load(cities_file)

        print("Largest cities in the US by population:")
        for index, entry in enumerate(cities_data):
            print(f"{index + 1}: {entry['name']} - {entry['pop']}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()
```

## Handling Exceptions

Parsing files - especially if you didn't create them - is often tricky, and you're going to have to deal with less-than-perfect data. For example, go into your `cities.json` file and delete the last `]` character. Run your program again.

```bash
(env) $ python file_execise.py
```

Helpfully, the library told you (on the last line) approximately what is wrong and where. It also provides a Traceback to help you see what happened, starting with your `main()` function, which called `json.load(cities_file)`, and into the functions used internally to the `json` library. This will become more useful once you start writing your own libraries, so practice reading and understanding your Tracebacks.

But let's say we're writing a web app or user-facing app and don't want our users to see Tracebacks (they can be scary if you're not a programmer, as well as risk your security by leaking information about your software). Let's catch that `JSONDecodeError` and return something prettier.

```python
# file_execise.py

import json

def main():
    with open("cities.json") as cities_file:
        try:
            cities_data = json.load(cities_file)

            print("Largest cities in the US by population:")
            for index, entry in enumerate(cities_data):
                print(f"{index + 1}: {entry['name']} - {entry['pop']}")

        except json.decoder.JSONDecodeError as error:
            print("Sorry, there was an error decoding that json file:")
            print(f"\t {error}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()
```

Here, we've wrapped our business logic in another scope - the `try - except` block. For the `except`, we reach into the `json` library and reference the `JSONDecodeError` that's part of the `decoder` module. We assign it to `error` so that we can reference it later. We then print out the entire error, prefixed with a tab character `\t` to make it a little easier to read. Voilà, we've caught our error and reported it to the user with (hopefully) helpful information (but not too much information). Run your program again.

Let's review what we learned today and put it all together.

For the final exercise of today, we're going to write a small program that requests the top repositories from GitHub, ordered by the number of stars each repository has, then we're going to print the results to our terminal. Create a new file called `day_one.py`.

{{% notice note %}}
You may need to install the `requests` library using `python -m pip install requests`. You may see `pip` used directly, but using `python -m pip` is [recommended by Python](https://docs.python.org/3/installing/index.html).
{{% /notice %}}

Let's start with our key function, the one that gets the data from the [GitHub API](https://developer.github.com/v3/search/). Use the `requests` library to do a GET request on the GitHub search API URL ("https://api.github.com/search/repositories"). Use `if __name__ == "__main__"` to check to make sure we're running the file directly, and to call our function. Don't forget to `import requests`

Run your exercise:
```bash
(env) $ python day_one.py
```

### Getting a Response

Looks like we got a response from the GitHub API! Looks like we hit an error - we're missing search parameter. Checking the `documentation_url` that GitHub helpfully provides, we can see that we're missing the parameter `q`, which contains search keywords. Let's hardcode a query string to find repos with more than 50,000 stars and try again. We'll add our query string to the `parameters` dict as `q`, and pass it to the `params` argument of `requests.get()`


### Response Parsing

Woah, we got a huge response from GitHub, including metadata for 33 repos. Let's parse it out so we can make better sense of what we have - use `response.json()` to get the returned data in json format. We see that GitHub returns a list called `items` in our response, so let's `return` that. Then, in your main function, loop through it and print out the important bits.


### Narrowing it Down

We should now have a much more readable list of 33 or so repos, along with their number of stars. Let's narrow down our search a bit. To use multiple search keywords, we'll have to programatically construct our query string. Using the GitHub API documentation, let's make a new function to construct a query string for the repository search endpoint that searches for any number of languages, and limits our query to repos with more than 50,000 stars.


Now, let's call our new `create_query()` function from `repos_with_most_stars()`, replacing our hardcoded query string. Add a `languages` argument so that we can pass in a list of languages to use to create our query. Also add `sort` and `order` parameters, which we'll hardcode to "stars" and "desc" for now.


Finally, let's add a `languages` list to limit which languages we're interested in, and pass it to `repos_with_most_stars()`. Now, when we call our `repos_with_most_stars()` function with `["python", "javascript", "ruby"]` as our languages, the `create_query()` function will output create a query string that looks like `q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc`. Because this is a simple GET request, this gets appended to our `gh_api_repo_search_url`, so our actual request URL is `https://api.github.com/search/repositories?q=stars:>50000+language:python+language:javascript+language:ruby+&sort=stars&order=desc`.

Run your program.

### Cleaning Up and Handling Errors

Looking good, we now have a sorted list of the top python, javascript, and ruby repos. Let's do a little bit of clean up and error handling. We might not always want to sort by "stars" or order by "desc", so move those to keyword arguments. That way, they'll be good defaults, but if someone calling our `repos_with_most_stars` function wants to override them, they can.


Next, we should handle any errors we might run into with the API. Maybe you've gotten one already. Let's add some basic error handling on the response's HTTP status code. We'll check for a `403`, a common error that GitHub uses to tell you that you're hitting their API too quickly, and `raise` and error. We'll also `raise` an error if the status code is anything but `200` (success).


There, your code should do the same thing, but should handle errors much better. The final code can be found below.

## The Standard Library

The Python standard library has a huge number of packages - no matter what you want to do, there's probably a package included. Let's practice using some of the more common ones. Create a new file and use the `os` module to see if you can get a file listing for the folder your new file is in.

```python
# libraries_exercise.py

import os

my_folder = os.getcwd()
print(f"Here are the files in {my_folder}:")

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f" - {entry.name}")
```

```bash
(env) $ python libraries_exercise.py
```

`sys` is another commonly useful library, giving you access to some variables and functions used or maintained by the Python interpreter. Let's try using `sys` to get the arguments passed into our program from the command line, and to figure out what kind of computer we're using:

```python
# libraries_exercise.py

import sys

arguments = sys.argv
print(f"We received the following arguments:")

for arg in arguments:
    print(f" - {arg}")

print(f"We are running on a '{sys.platform}' machine")
```

## Pypi

PyPI (the Python Package Index) is an awesome service that helps you find and install almost any 3rd-party Python package. You can browse the site at [PyPI.org](https://PyPI.org/) but most of the time you will probably interact with it through Python's `pip` command line tool.

For example, earlier you may have installed the `requests` module. If you search `pip` for `requests`, you'll see every package in the index containing the word requests:

```bash
(env) $ python -m pip search requests
requests-hawk (1.0.0)                  - requests-hawk
requests-dump (0.1.3)                  - `requests-dump` provides hook functions for requests.
requests-aws4auth (0.9)                - AWS4 authentication for Requests
...
```

We just want the one named `requests`, so we'll install it with the `install` keyword. If you don't have it installed, `pip` will install it for you. If you installed it earlier, you'll see something like this:

```bash
(env) $ python -m pip install requests
Requirement already satisfied: requests in /usr/local/lib/python3.7/site-packages (2.21.0)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/lib/python3.7/site-packages (from requests) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/site-packages (from requests) (2019.3.9)
Requirement already satisfied: idna<2.9,>=2.5 in /usr/local/lib/python3.7/site-packages (from requests) (2.8)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /usr/local/lib/python3.7/site-packages (from requests) (1.24.1)
```


## Adding Tests

Python comes with a very easy-to-use `unittest` library built in. Write a simple function that accepts two numbers, and returns `True` if the first number is evenly divisible by the second.

```python
# divisible.py

def divisible_by(check_number, divisor):
    return check_number % divisor == 0
```

Save your file as `divisible.py`. In a second file called `test_divisible.py`, create a `TestCase` using the `unittest` framework and use asserts to verify that the `divisible_by()`function returns the correct result. Don't forget to import your `divisible_by()` function.

```python
# test_divisible.py

import unittest
from divisible import divisible_by

class TestCase(unittest.TestCase):

    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 2))
        self.assertTrue(divisible_by(10, 3))


if __name__ == '__main__':
    unittest.main()
```

Name your file `test_divisible.py` and run it:

```bash
(env) $ python test_divisible.py --verbose
```

You should have gotten an error: `AssertionError: False is not true` caused by `self.assertTrue(divisible_by(10, 3))`. Makes sense, because 10 is not evenly divisible by 3.

{{% notice tip %}}
Change `self.assertTrue` to `self.assertFalse` and your test should pass.
{{% /notice %}}

```bash
(env) $ python test_divisible.py --verbose
test_divisible_by (__main__.TestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Solutions

### Running Code

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
[{'name': 'New York', 'pop': 8550405}, {'name': 'Los Angeles', 'pop': 3971883}, {'name': 'Chicago', 'pop': 2720546}, {'name': 'Houston', 'pop': 2296224}, {'name': 'Philadelphia', 'pop': 1567442}]
```

```bash
(env) $ python file_execise.py
Largest cities in the US by population:
1: New York - 8550405
2: Los Angeles - 3971883
3: Chicago - 2720546
4: Houston - 2296224
5: Philadelphia - 1567442
```

```bash
(env) $ python file_execise.py
Largest cities in the US by population:
1: New York - 8550405
2: Los Angeles - 3971883
3: Chicago - 2720546
4: Houston - 2296224
5: Philadelphia - 1567442
The file is now closed.
```

{{%/expand%}}

### Handling Exceptions

Delete the last `]` character from your `cities.json` file and run your program again.

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
Traceback (most recent call last):
  File "file_execise.py", line 14, in <module>
    main()
  File "file_execise.py", line 5, in main
    cities_data = json.load(cities_file)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py", line 296, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/decoder.py", line 353, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 21 column 1 (char 234)
```
{{%/expand%}}


  \
Now try wrapping the JSON decoding in a `try... except` block.

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python file_execise.py
Sorry, there was an error decoding that json file:
     Expecting ',' delimiter: line 21 column 1 (char 234)
The file is now closed.
```
{{%/expand%}}

  \
Use the `requests` library to do a GET request on the GitHub search API.

{{%expand "You should have something like this:" %}}

```python
# file_exercise.py

import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    response = requests.get(gh_api_repo_search_url)

    print(response.text)


if __name__ == "__main__":
    repos_with_most_stars()
```
{{%/expand%}}

  \
Run your GitHub search exercise.
{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
{"message":"Validation Failed","errors":[{"resource":"Search","field":"q","code":"missing"}],"documentation_url":"https://developer.github.com/v3/search"}
```

{{%/expand%}}


### Getting a Response

{{%expand "You should have something like this:" %}}

```python
# day_one.py

import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    parameters = {"q": "stars:>50000"}
    response = requests.get(gh_api_repo_search_url, params=parameters)

    print(response.text)


if __name__ == "__main__":
    repos_with_most_stars()
```
{{%/expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
{"total_count":33,"incomplete_results":false,"items":[{"id":28457823,"node_id":"MDEwOlJlcG9zaXRvcnkyODQ1NzgyMw==","name":"freeCodeCamp"...
```
{{%/expand%}}

### Response Parsing

{{%expand "You should have something like this:" %}}

```python
# day_one.py

import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    parameters = {"q": "stars:>50000"}
    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()

    return response_json["items"]


if __name__ == "__main__":
    results = repos_with_most_stars()

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```
{{%/expand%}}


{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
-> freeCodeCamp is a JavaScript repo with 298059 stars.
-> bootstrap is a JavaScript repo with 131410 stars.
-> vue is a JavaScript repo with 130168 stars.
-> react is a JavaScript repo with 124029 stars.
-> tensorflow is a C++ repo with 122328 stars.
-> free-programming-books is a None repo with 118241 stars.
-> awesome is a None repo with 103392 stars.
-> You-Dont-Know-JS is a None repo with 97587 stars.
...
```

{{%/expand%}}

#### Narrowing it Down

{{%expand "You should have something like this:" %}}

```python
# day_one.py
import requests

def create_query(languages, min_stars=50000):
    # An example search query looks like:
    # stars:>50000 language:python language:javascript

    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query

def repos_with_most_stars(languages):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    sort = "stars"
    order = "desc"
    parameters = {"q": query, "sort": sort, "order": order}

    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()

    return response_json["items"]

if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```

{{%/expand%}}

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python day_one.py
-> freeCodeCamp is a JavaScript repo with 298059 stars.
-> bootstrap is a JavaScript repo with 131410 stars.
-> vue is a JavaScript repo with 130169 stars.
-> react is a JavaScript repo with 124029 stars.
-> d3 is a JavaScript repo with 82945 stars.
-> javascript is a JavaScript repo with 82531 stars.
-> react-native is a JavaScript repo with 74828 stars.
-> create-react-app is a JavaScript repo with 64748 stars.
-> awesome-python is a Python repo with 63734 stars.
-> angular.js is a JavaScript repo with 59413 stars.
-> Font-Awesome is a JavaScript repo with 59051 stars.
-> system-design-primer is a Python repo with 58972 stars.
-> node is a JavaScript repo with 58863 stars.
-> axios is a JavaScript repo with 56121 stars.
-> public-apis is a Python repo with 53212 stars.
-> jquery is a JavaScript repo with 51040 stars.
```

{{%/expand%}}

#### Cleaning Up and Handling Errors

{{%expand "You should have something like this:" %}}

```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}

    response = requests.get(gh_api_repo_search_url, params=parameters)
    response_json = response.json()

    return response_json["items"]
```

```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)

    # Define the parameters we want to be part of our URL
    parameters = {"q": query, "sort": sort, "order": order}

    # Pass in the query and the parameters as part of the request.
    response = requests.get("https://api.github.com/search/repositories", params=parameters)
    status_code = response.status_code

    # Check if the rate limit was hit. Applies only for students running this code
    # in the in-person course.
    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}.")
    else:
        response_json = response.json()
        records = response_json["items"]
        return records
```
{{%/expand%}}

{{%expand "The final code, with additional comments, can be found here:" %}}


```python
"""
A small Python program that uses the GitHub search API to list
the top projects by language, based on stars.

GitHub Search API documentation: https://developer.github.com/v3/search/

Additional parameters for searching repos can be found here:
https://help.github.com/en/articles/searching-for-repositories#search-by-number-of-stars

Note: The API will return results found before a timeout occurs,
so results may not be the same across requests, even with the same query.

Requests to this endpoint are rate limited to 10 requests per
minute per IP address.
"""

import requests


def create_query(languages, min_stars=50000):
    """
    Create the query string for the GitHub search API,
    based on the minimum amount of stars for a project, and
    the provided programming languages.

    An example search query looks like:
    stars:>50000 language:python language:javascript
    """
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)

    # Define the parameters we want to be part of our URL
    parameters = {"q": query, "sort": sort, "order": order}

    # Pass in the query and the parameters as part of the request.
    response = requests.get(gh_api_repo_search_url, params=parameters)
    status_code = response.status_code

    # Check if the rate limit was hit. Applies only for students running this code
    # in the in-person course.
    if status_code == 403:
        raise RuntimeError("Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(f"An error occurred. HTTP Status Code was: {status_code}.")
    else:
        response_json = response.json()
        records = response_json["items"]
        return records


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")
```
{{%/expand%}}

### The Standard Library

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python libraries_exercise.py
Here are the files in /Users/nina/Desktop/libraries_exercise:
 - libraries_exercise.py
```

```bash
(env) $ python libraries_exercise.py argument1 hello world "this is one argument"
We received the following arguments:
 - libraries_exercise.py
 - argument1
 - hello
 - world
 - this is one argument
We are running on a 'darwin' machine
```
Note: if the string returned by `sys.platform` isn't what you expect, take a look at the [sys documentation](https://docs.python.org/3/library/sys.html).

{{% /expand%}}

### Adding Tests

{{%expand "Here's what you should have seen on your command line:" %}}

```bash
(env) $ python test_divisible.py --verbose
test_divisible_by (__main__.TestCase) ... FAIL

======================================================================
FAIL: test_divisible_by (__main__.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_divisible.py", line 8, in test_divisible_by
    self.assertTrue(divisible_by(10, 3))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```
{{% /expand%}}