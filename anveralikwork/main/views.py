from django.shortcuts import render


def index(request):
    data = {
        "title": "Main page",
    }
    return render(request, "main/index.html", data)
