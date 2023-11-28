from django.shortcuts import redirect, render
from django.contrib import messages
from all.forms import *

# Create your views here.
def home(request):
    context = {
        # "title":"Contact"
    }
   
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, 'Your quote request has been sent successfully. Thank you!')
            return redirect('home')
        else:
            messages.error(request, "Your information was not submitted!.")
        
   
    else:
        form = ContactForm()
    context["form"] = form
    return render(request,"home.html", context)

def contact(request):
    context = {
        "title":"Contact"
    }
   
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, 'Your quote request has been sent successfully. Thank you!')
            return redirect('contact')
        else:
            messages.error(request, "Your information was not submitted!.")
        
   
    else:
        form = ContactForm()
    context["form"] = form
    return render(request,"contact.html", context)

def projects(request):
    return render(request,"projects.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def sendemail(request):
    if request.method == "POST":
        pass
    return redirect('home')