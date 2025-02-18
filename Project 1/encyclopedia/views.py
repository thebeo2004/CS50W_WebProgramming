from django.shortcuts import render
from django.http import HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    
    if content is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })