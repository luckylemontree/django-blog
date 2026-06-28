from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Stores a single blog post, related to :model:`auth.User` (author).

    Posts are created and edited by the superuser through the Django
    admin. Only posts with ``status`` set to Published (1) are shown to
    visitors; the :view:`blog.views.PostList` and
    :view:`blog.views.post_detail` views filter on ``status=1``.

    **Fields**

    ``title``
        Headline of the post. Unique, max 200 characters.
    ``slug``
        URL-friendly identifier used in the post's URL. Unique.
    ``author``
        ForeignKey to :model:`auth.User`. Deleting the user cascades to
        delete their posts. Reverse accessor: ``user.blog_posts``.
    ``featured_image``
        Cloudinary-hosted header image. Defaults to ``'placeholder'`` so
        the template can fall back to a local default image.
    ``content``
        The main body of the post.
    ``excerpt``
        Optional short summary (``blank=True``) shown in listings.
    ``status``
        Integer choice from ``STATUS``: 0 = Draft (hidden), 1 = Published
        (visible). Defaults to Draft.
    ``created_on``
        Timestamp set automatically when the post is created.
    ``updated_on``
        Timestamp refreshed automatically on every save.

    **Meta**

    Posts are ordered by ``created_on`` (oldest first).
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
        )

    featured_image = CloudinaryField('image', default='placeholder')

    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment on a :model:`blog.Post`, by a
    :model:`auth.User`.

    Comments are submitted by logged-in users from the post detail page.
    A new comment starts unapproved (``approved=False``) and is hidden
    from other visitors until the superuser approves it in the admin.
    Authors can edit or delete their own comments via
    :view:`blog.views.comment_edit` and
    :view:`blog.views.comment_delete`; editing resets ``approved`` to
    ``False`` so the change is re-moderated.

    **Fields**

    ``post``
        ForeignKey to :model:`blog.Post`. Deleting the post cascades to
        delete its comments. Reverse accessor: ``post.comments``.
    ``author``
        ForeignKey to :model:`auth.User`. Deleting the user cascades to
        delete their comments. Reverse accessor: ``user.comments``.
    ``body``
        The text content of the comment.
    ``approved``
        Boolean, ``False`` by default. Only approved comments are
        counted and shown publicly.
    ``created_on``
        Timestamp set automatically when the comment is created.

    **Meta**

    Comments are ordered by ``created_on`` (newest first).
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]



    def __str__(self):
        return f"Comment  {self.body}  by  {self.author}"
