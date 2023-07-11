
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

from .forms import SignupForm, BlogForm

dt = datetime.today()

def index(request):
    return render(request, "dogBlog/index.html", context={"date":dt})


def signup(request):
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        
        if signup_form.is_valid():
            print(signup_form.cleaned_data)
            
        return HttpResponseRedirect(request.path)    
            
    else:
        signup_form = SignupForm()
                
    return render(request, "dogBlog/signup.html", context={"signup_form":signup_form})


def blogpost(request):
    
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        
        if blog_form.is_valid():
            print(blog_form.cleaned_data)
        
        return HttpResponseRedirect(request.path)    
            
    else:
        blog_form = BlogForm()
                
    return render(request, "dogBlog/blogpost.html", context={"blog_form":blog_form})