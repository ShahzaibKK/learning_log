from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import NewTopic, NewEntry
from django.http import HttpRequest

# from django.db.models.query import QuerySet


# Create your views here.
def index(request):
    """The home page for learning logs"""
    return render(request, "learning_logs/index.html")


def topics(req):
    topics = Topic.objects.order_by("date")
    context = {"topics": topics}
    return render(req, "learning_logs/topics.html", context)


def topic(req, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entires = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entires}
    return render(req, "learning_logs/topic.html", context)


def new_topic(req: HttpRequest):
    if req.method != "POST":
        form = NewTopic()
    else:
        form = NewTopic(data=req.POST)
        form.is_valid()
        form.save()
        return redirect("learning_logs:topics")

    context = {"form": form}
    return render(req, "learning_logs/new_topic.html", context)


def new_entry(req: HttpRequest, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if req.method != "POST":
        form = NewEntry()
    else:
        form = NewEntry(data=req.POST)
        form.is_valid()
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return redirect("learning_logs:topic", topic_id=topic_id)

    context = {"form": form, "topic": topic}
    return render(req, "learning_logs/new_entry.html", context)


def edit_entry(req: HttpRequest, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if req.method != "POST":
        form = NewEntry(instance=entry)
    else:
        form = NewEntry(instance=entry, data=req.POST)
        form.is_valid()
        form.save()
        return redirect("learning_log:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(req, "learning_logs/edit_entry.html", context)
