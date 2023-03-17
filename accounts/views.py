from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


def register(req):
    if req.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=req.POST)

        if form.is_valid():
            new_user = form.save()
            login(req, new_user)
            return redirect("learning_logs:index")

    context = {"form": form}
    return render(req, "registration/register.html", context)
