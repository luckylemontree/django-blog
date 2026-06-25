from django.shortcuts import render
from .models import About


def about_detail(request):
    """
    Display the most recent :model:`about.About` instance.

    **Context**

    ``about``
        The most recently updated instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """
    about = About.objects.order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
