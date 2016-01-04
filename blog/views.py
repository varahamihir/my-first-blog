from django.shortcuts import render

from django.template import loader,Context
from django.http import HttpResponse
from .models import post

def index(request):
  posts=post.objects.all()
  t=loader.get_template("blog/index.html")
  context={'posts':posts}
  return HttpResponse(t.render(context,request))
  