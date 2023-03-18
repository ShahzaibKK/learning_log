from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import NewTopic, NewEntry
from django.http import HttpRequest, Http404
from django.contrib.auth.decorators import login_required

# from django.db.models.query import QuerySet


# my owner_check_function
def check_topic_owner(topic, req):
    """owner check bro"""
    if topic.owner != req.user:
        raise Http404


# Create your views here.
def index(request):
    """The home page for learning logs"""
    return render(request, "learning_logs/index.html")


@login_required
def topics(req: HttpRequest):
    topics = Topic.objects.filter(owner=req.user).order_by("date")
    context = {"topics": topics}
    return render(req, "learning_logs/topics.html", context)


@login_required
def topic(req, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, req)
    entires = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entires}
    return render(req, "learning_logs/topic.html", context)


@login_required
def new_topic(req: HttpRequest):
    if req.method != "POST":
        form = NewTopic()
    else:
        form = NewTopic(data=req.POST)
        form.is_valid()
        new_topic = form.save(commit=False)
        new_topic.owner = req.user
        new_topic.save()

        return redirect("learning_logs:topics")

    context = {"form": form}
    return render(req, "learning_logs/new_topic.html", context)


@login_required
def new_entry(req: HttpRequest, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, req)
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


@login_required
def edit_entry(req: HttpRequest, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, req)

    if req.method != "POST":
        form = NewEntry(instance=entry)
    else:
        form = NewEntry(instance=entry, data=req.POST)
        form.is_valid()
        form.save()
        return redirect("learning_log:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(req, "learning_logs/edit_entry.html", context)
