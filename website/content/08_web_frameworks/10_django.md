+++
title = "Django"
date = 2020-08-29T17:05:03-07:00
weight = 10
+++

Since this course is targeted towards a more advanced audience, we're going to jump into Django. If you'd like to learn more about Flask instead, watch the last chapter of the [Intermediate Python Course](https://frontendmasters.com/courses/intermediate-python/) on Frontend Masters, or review the [final exercise](https://www.learnpython.dev/03-intermediate-python/80-web-frameworks/).

We're going to work on a basic blog that'll help you understand the basic concepts of Django.


### Grab project code

Instead of starting from scratch, let's start with a project that already has an app, which is the foundation we need to work on our blog.

If you need to start a new Django project from scratch, I recommend following the steps on the [official Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) for building your first app.

Go to your home or project directory, and `git` clone the files for our Django blog. Not comfortable with `git`? [Download the files](https://github.com/nnja/practical_blog/archive/main.zip) instead. 

```bash
$ cd ~
$ git clone https://github.com/nnja/practical_blog.git
$ cd practical_blog
```

Let's create and activate a brand new virtual environment for our Django blog.

Take a look at the `requirements.txt` file, it contains a (short) list of dependencies for this project.

We're going to install these dependencies in our newly created virtual environment with the `pip install -r` command.

Note, if you're already in a virtual environment, type `deactivate` or open a new terminal window.

```bash
$ python -m venv env
$ source env/bin/activate
(env) $ python -m pip install -r requirements.txt
```

Next, we'll need to create the database and database tables. We'll do this with the migrate command.

```bash
(env) $ python manage.py migrate
```

Finally, run the server:

```bash
(env) $ python manage.py runserver
```

Your site should now be available at [http://localhost:8000/](http://localhost:8000/)



<!-- 
### Initial Setup

We'll need to do a few things to install Django on our systems. We'll be using Django 3.1, the latest version as of October 2020.

Once Django is installed, we can run the new project setup tool to create our project structure.

With your virtual environment activated in your project folder enter:

```bash
(env) $ python -m pip install django==3.1  
```

This pulls down the latest version of Django 3.1 and installs it into your virtual environment.

Next, we're going to use a tool installed by Django called `django-admin` to create our project structure, and cd into the newly created directory.

```bash
(env) $ django-admin startproject testblog
(env) $ cd testblog
```

Now that we have the testblog project, we'll need to create a new app, named `blog`.

```bash
(env) $ python manage.py startapp blog 
```

A Django project can have multiple apps. For example, if your company has a website it might have multiple apps -- a blog, an e-commerce site, and more.

Your initial directory structure in `~/pyworkshop/practical_blog` should look something like this.

```bash
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── practical_blog
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

3 directories, 15 files
```

Instead of starting from scratch, download the file blog.zip and expand it into your ~/pyworkshop/myblog directory.

Let's make sure that everything worked by starting the server, then navigating to [http://localhost:8000](http://localhost:8000).

```bash
(env) $ python manage.py runserver
```

You should see:

![](/images/django/success.png) -->