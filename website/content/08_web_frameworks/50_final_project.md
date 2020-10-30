+++
title = "Final Project Practice"
date = 2020-08-29T17:05:30-07:00
weight = 50
+++

### Installing requirements

If you haven't already, grab the code for our blog from GitHub, create a virtual environment, and install the project requirements.

Make sure you checkout the `final_practice` branch.

```bash
$ git clone https://github.com/nnja/practical_blog.git
$ git checkout final_practice
$ cd practical_blog
$ python3 -m venv env
$ source env/bin/activate
(env) $ python -m pip install -r requirements.txt
```

Next, start the development server

```bash
(env) $ python manage.py runserver
```

You should see:
```text
Django version 3.1, using settings 'practical_blog.settings'
Starting development server at http://127.0.0.1:8000/
```

Visit the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to make sure everything started correctly.

### Final Exercise

For the final exercise, we're going to:
1. Sort our blog posts by reverse chronological order
1. Add an`is_draft` flag that allows you to start working on blog posts but keep them from being seen by readers.
1. (If time allows) Write additional unit tests to make sure that `is_draft` is working as expected.


### Sorting in reverse order

We can provide a default sort order for our model by adding some metadata through it via Django's nested Meta class.

in `blog/models.py`, add:

```python
from django.db import models

class Post(models.Model):
    # ... fields here.

    class Meta:
        ordering = ('-created_at', )
```

Notice a few things:
1. This is a **nested** class under `Post`, so make sure it's indented properly
1. `ordering` expects a `tuple`, so don't forget that trailing comma. 

Make sure your server is running

```bash
python manage.py runserver      
```

Reload the page. Your posts should now be in reverse chronological order.

### Adding `is_draft`

First, we'll need to add a new `is_draft` flag to our post model, make migrations, and run them.

We'll provide a default value of `False`, and Django will fill in that column in the database for us when it runs the migration.

In `blog/models.py` add the following field to the `Post` class.

```python
is_draft = models.BooleanField(default=False)
```

Make migrations for the blog app, then run them:

```python
(env) $ python manage.py makemigrations blog 
(env) $ python manage.py migrate blog 
```

Now, verify that the current blog posts have a draft status of `False` by using the Django shell command, and importing the models.

```bash
(env) $ python manage.py shell
```

```python
>>> from blog.models import Post
```

Remember, `Post.objects.all()` will return all of the models in our database as a `QuerySet`. You can loop over the items, just like you would a list to examine their values.

```python
>>> Post.objects.all()
<QuerySet [<Post: First Post!>, <Post: second blog post>]>
```

#### Modifying our views to not return draft posts

We'll need to modify our views so that draft posts aren't visible to the user.

In class based views, all you need to do is define a custom queryset.

In `blog/views.py`:

```python
class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_draft=False)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(is_draft=False)
```

#### (Optional, if time) Writing more Unit Tests

Now, if you have time, you'll want to write some unit tests to verify that posts in draft status aren't visible on the main page, and that trying to get to the detail page for a draft post will return in a 404.

If you need some hints, check out the `final_practice_solutions` branch.


### Going Further with Django
If you'd like to go even further on your Django journey after the course, try some of the following challenges that are outside the scope of today's lesson on your own.

Here are a few ideas that you can start with:
- Add a simple form to submit comments (use DjangoGirls as a guide https://tutorial-extensions.djangogirls.org/en/homework_create_more_models)
- Add Blog post tags. Each blog post can be tagged with different categories. Add a page to the blog with a list of tags along with the Posts in each category.
- Add pagination so that only 10 posts show on the main page, have a previous and a next button.
- Make the blog look nicer by styling it with CSS.

Note: If you'd like to see a standalone Django course, you can request it from Frontend Masters via [Twitter](https://twitter.com/FrontendMasters) or e-mail at support@frontendmasters.com.