---
title: "Django Tests"
date: 2020-10-25T23:05:30-07:00
weight: 40
---

Tests in Django inherit from a special class, `from django.test import TestCase`, and can be run using the manage.py command.

Put your tests in `blog/tests.py`.

```python
from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class PostListViewTests(TestCase):
    def test_posts_visible(self):
        post = Post.objects.create(
            title="A title", body="Blog content.", slug="test-slug"
        )

        url = reverse("posts")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        # Special Django Helper Method
        self.assertQuerysetEqual(response.context["post_list"], ["<Post: A title>"])

        # Test the webpage content contains our post body.
        self.assertContains(response, "Blog content.")
```

And then run them:

```bash
(env) $ python manage.py test blog
```