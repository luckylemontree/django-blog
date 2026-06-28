from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm



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
    
    



    if request.method == "POST":        
        collaborate_form = CollaborateForm(data=request.POST)     
        if collaborate_form.is_valid():                     
           collaborate_form.save()
           messages.success(
               request, 
              'Collaboration request received! I endeavour to respond within 2 working days.'
           )

    collaborate_form = CollaborateForm()


    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form":collaborate_form,},
    )
   