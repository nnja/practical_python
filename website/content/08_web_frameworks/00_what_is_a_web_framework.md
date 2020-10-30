+++
title = "What are web frameworks?"
date = 2020-08-29T17:04:58-07:00
weight = 1
+++

Web frameworks are designed to support creating web applications while simplifying and abstracting away a lot of what happens under the hood. They provide a lot of the plumbing for you, allowing you focus building your application itself.

### Types of Web Frameworks in Python

There are two popular web frameworks in Python. Both are in active development and have vibrant communities that welcome beginners.

#### Django

Django is a fully-featured, high-level framework for building web apps. Django focuses on automating as much as possible, and many large-scale sites like Instagram run on Django. Because Django provides so much out of the box, it's also considered quite an opinionated framework.

Django bills itself as the web framework for perfectionists with deadlines.

What's included in Django?
- A Database ORM (Object Relational Model) to make working with databases as easy as working with Python Code
- An easy-to-build-upon Admin back-end to allow for easy content management
- Built-in user authentication
- A template language
- Protection against common security vulnerabilities like cross-site scripting attacks and SQL injection
- And much more

#### Flask

Flask is a "microframework" for Python, allowing users to make basic backend APIs and web apps with far less code. Flask is easier for beginners to understand and setup, and is less opinionated. The drawback is that as you start wanting to add additional components to your application - such as databases, authentication, and other layers - you'll need to use plugins or third-party packages. Flask won't provide these for you out of the box.

{{% notice note %}}
If neither Flask or Django are right for you, there are many more frameworks for Python. You can find a more detailed list [here](https://wiki.python.org/moin/WebFrameworks).
{{% /notice %}}

### Frontend Integrations

You're not required to use templating in either Django or Flask. Both frameworks work well when paired with modern frontend technologies, like React, Angular, and Vue. Learn more about these frameworks on [Frontend Masters](https://frontendmasters.com/courses/).