from django.shortcuts import render
from django.views import generic
from .models import About
from django.shortcuts import render, get_object_or_404

# Create your views here.
class AboutList(generic.ListView):
    queryset = About.objects.all()
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest = About.objects.order_by("-updated_on").first()
        context["about"] = latest
        context["update_time"] = latest.updated_on if latest else None
        return context


def about_detail(request, slug):
    """
    Display an individual :model:`about.`.

    **Context**

    ``about``
        An instance of :model:`blog.About`.

    **Template:**

    :template:`about/about.html`
    """

    queryset = About.objects.all()
    about = get_object_or_404(queryset, slug=slug)
    update_time = About.objects.order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {"about": about, "update_time": update_time},
    )
