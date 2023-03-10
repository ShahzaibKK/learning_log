from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """The home page for learning logs"""
    return render(request, "learning_logs/index.html")


def topics(req):
    topics = Topic.objects.order_by("date")
    context = {"topics": topics}
    return render(req, "learning_logs/topics.html", context)
