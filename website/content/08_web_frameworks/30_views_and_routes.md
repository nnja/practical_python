---
title: "Views, Routes, Templates"
date: 2020-10-25T12:51:37-07:00
weight: 30
---

Views and routes allow us to map URLs in our web application to pages, API endpoints, and more.

Currently, our blog has 3 different sections.
1. The index at `/` which displays all of our posts.
2. Detail pages for each blog post, available at / followed by the post slug
3. A static `about` page in the header.

### Routes

Routes tell the web application what URLs different sections of the website will be found at.

We have routes defined in two places in our application.

One at the project level in `practical_blog/urls.py`, and one at the app level at `blog/urls.py`

### Templates

We have three simple templates for our blog, and one CSS file.

Django has an odd directory structure for where templates and static files need to live to be discoverable.

For templates, it's `blog/templates/blog/`, and for static files `blog/static/blog/`

```
.
├── blog
│   ├── static
│   │   └── blog
│   │       └── css
│   │           └── blog.css
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── post_detail.html
│   │       └── post_list.html
```

Our base template is in `base.html`, containing all the shared elements of the various other pages like headers and footers.

Template tags are special directives that are interpreted by Django in html files, and they're contained inside of curly braces & the percent symbol, like this: `{% %}`

In `base.html` we've included some template tags that define where content that uses this base template needs to be inserted.


```python
    <!-- Content blocks let us use base.html as a template. -->
    {% block content %}
    {% endblock %}
```

Now, check `post_detail.html`. We need to specify which base template we're extending from, in this case it's `blog/base.html`, and specify where the content we want inserted starts and ends. 

```python
{% extends 'blog/base.html' %}
{% block content %}
<article class="o-box c-card c-post">
    <h2 class="c-post__title">{{ post.title }}</h2>
    <h6 class="c-post__meta">{{ post.created_at | date:'Y-m-d'}}</h6>
    <p>
        {{ post.body | safe}}
    </p>
</article>
{% endblock %}
```

We're also using a `post` variable, that's passed in from the view in the context. 

### Views

Views are defined in `blog/views.py`

We're using three different techniques for templates. 

The about page has no dynamic content in it, so we're just loading it from a template.

```python
def about(request):
    template = loader.get_template("blog/about.html")
    return HttpResponse(template.render(request))
```

In the index view, we're creating a query, and passing that in to the template with the name `post_list`.

```python
def index(request):
    posts = Post.objects.all()
    context = {"post_list": posts}
    return render(request, "blog/post_list.html", context=context)
```

For the detail `post()` view, we're using a shortcut method called `get_object_or_404`. If a post with that slug doesn't exist, it'll redirect straight to a 404 page. 

```
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
```

### Class based views

Because these patterns are so common in Django, the framework features shortcuts called Class Based Views for them. To switch to class based views, you need to import them, and just provide the name of the model we'll be using.

Note that we don't need to specify a template name because our templates are named how Django expects, in this case `post_list.html` and `post_detail.html`. If you named your templates something else, you'd need to specify the name in the class definition.

The new `blog/views.py` is in the class_based_views branch, or you can find the new simplified code below:

```python
from django.views.generic import DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

```
