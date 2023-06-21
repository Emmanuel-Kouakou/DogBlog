
# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

dt = datetime.today()

def index(request):
    return render(request, "dogBlog/index.html", context={"date":dt})