from news.models import Post
from django.shortcuts import render_to_response
from django.utils import timezone
import datetime

def current_datetime(request):
    current_date = datetime.datetime.now()

    return render_to_response('current_datetime.html', locals())

def news(request):
    name = "News"
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    print posts
    return render_to_response('news.html', locals())

def about(request):
    name = "About"
    return render_to_response('about.html', locals())

def lessons(request):
    name = "Lessons"
    return render_to_response('lessons.html', locals())

def work(request):
    name = "Work"
    return render_to_response('work.html', locals())

def media(request):
    name = "Media"
    return render_to_response('media.html', locals())

def contact(request):
    name = "Contact"
    return render_to_response('contact.html', locals())
