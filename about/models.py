from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores the content displayed on the site's About page.

    The superuser creates and edits these entries through the Django
    admin. The :view:`about.views.about_detail` view renders the
    entry, so in practice the site has a single "current" About entry
    even though the model allows several.

    **Fields**

    ``title``
        Short heading for the entry. Unique, max 200 characters.
    ``content``
        The main body text shown on the About page (free-form text).
    ``profile_image``
        A Cloudinary-hosted image. Defaults to ``'placeholder'`` when no
        image has been uploaded, which the template uses to fall back to
        a local default image.
    ``created_on``
        Timestamp set once, automatically, when the entry is created.
    ``updated_on``
        Timestamp refreshed automatically on every save.

    **Meta**

    Entries are ordered by ``created_on`` (oldest first).
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    profile_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written on {self.created_on}"

class CollaborateRequest(models.Model):
    """
    Stores a collaboration request submitted from the About page.

    A site visitor fills in the collaboration form on the About page;
    each submission is saved as one instance of this model. The
    superuser reviews incoming requests in the Django admin and uses the
    ``read`` flag to track which ones have already been actioned.

    **Fields**

    ``name``
        Name of the person making the request. Max 200 characters.
    ``email``
        Reply-to email address, validated as a well-formed email.
    ``message``
        The body of the collaboration request (free-form text).
    ``read``
        Boolean flag, ``False`` by default, set to ``True`` once the
        superuser has reviewed/handled the request.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default = False)

    def __str__(self):
        return f"Collaboration request from {self.name}"